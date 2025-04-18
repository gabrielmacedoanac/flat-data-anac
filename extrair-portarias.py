import asyncio
import aiohttp
import csv
import json
import os
import pandas as pd
import re
from bs4 import BeautifulSoup
from pandas.io.formats.style import Styler

prefixo_url = "https://www.anac.gov.br/assuntos/legislacao/legislacao-1/portarias/"
anos = range(2024, 1973, -1)
dados_tabela = []
urls_acessadas = set()
regex_nao_imprimiveis = re.compile(r'[\x00-\x1F\x7F]')

## Parte 1 - Importar e criar dataframe

# Função para extrair dados das tabelas
def extrair_dados_tabela(tabela, ano):
    cabecalho = [th.get_text(strip=True) for th in tabela.find_all("th")]
    if ano == 2020: cabecalho[1], cabecalho[2] = cabecalho[2], cabecalho[1]
    if not dados_tabela: dados_tabela.append(cabecalho)
    
    for linha in tabela.find_all("tr"):
        valores = [
            " ".join([f"[{link.get_text(strip=True)}]({link['href']})" for link in coluna.find_all("a")]) 
            if coluna.find_all("a") else coluna.get_text(strip=True)
            for coluna in linha.find_all(["th", "td"])
        ]
        valores = [regex_nao_imprimiveis.sub(" ", str(v)).replace("|", " ").replace("  ", " ").strip() for v in valores]
        if valores and valores != cabecalho:
            if ano == 2020: valores[1], valores[2] = valores[2], valores[1]
            dados_tabela.append(valores)

# Função para extrair e formatar a data
def extrair_data(df):
    df['Data'] = df['Norma'].apply(lambda x: re.search(r'(\d{2}/\d{2}/\d{4})', str(x)).group(0) if re.search(r'(\d{2}/\d{2}/\d{4})', str(x)) else None)
    df['Data'] = df['Data'].fillna(df['Publicação'].apply(lambda x: re.search(r'(\d{2}/\d{2}/\d{4})', str(x)).group(0) if re.search(r'(\d{2}/\d{2}/\d{4})', str(x)) else None))
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce').dt.strftime('%Y-%m-%d')
    df['Data'] = df['Data'].mask(pd.isna(df['Data']), df['Publicação'].str.extract(r'(\d{2}/\d{2}/\d{4})', expand=False).apply(lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce').strftime('%Y-%m-%d') if pd.to_datetime(x, format='%d/%m/%Y', errors='coerce') is not pd.NaT else pd.NaT))
    df = df[['Data'] + [col for col in df.columns if col != 'Data']]
    return df

# Função assíncrona para acessar a URL e extrair dados
async def acessar_url(session, ano):
    url = f"{prefixo_url}{ano}"
    if url in urls_acessadas: return
    urls_acessadas.add(url)
    async with session.get(url) as r:
        if r.status == 200 and (t := BeautifulSoup(await r.text(), "html.parser").find("table", {"id": "tabela-normas"})):
            extrair_dados_tabela(t, ano)

async def fetch_all(): 
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(acessar_url(session, ano) for ano in anos))

if not asyncio.get_event_loop().is_running():
    asyncio.run(fetch_all())

# Cria um DataFrame a partir dos dados extraídos
if dados_tabela:
    df = pd.DataFrame(dados_tabela[1:], columns=["Norma", "Publicação", "Ementa", "Arquivo"])
    df = df.dropna(how='all').drop_duplicates()
    df = extrair_data(df)
    df = df[~((df['Norma'] == 'Norma') & (df['Publicação'] == 'Data') & (df['Ementa'] == 'Ementa') & (df['Arquivo'] == 'Arquivo'))]
    df = df.sort_values(by=['Data', 'Norma'], ascending=[False, False])
else:
    print("Nenhuma tabela foi extraída.")

## Parte 2 - exportar dados para vários formatos

# Exporta para Markdown
def exportar_markdown_simples(df, nome_arquivo):
    linhas = ["| " + " | ".join(df.columns) + " |"]
    linhas.append("| " + " | ".join(["---"] * len(df.columns)) + " |")
    for _, row in df.iterrows():
        linha_formatada = [regex_nao_imprimiveis.sub(" ", str(valor)).replace("|", " ").replace("  ", " ") for valor in row.values]
        linhas.append("| " + " | ".join(linha_formatada) + " |")
    with open(nome_arquivo, "w") as f:
        f.write("\n".join(linhas))
    print(f"Arquivo MD gerado com sucesso: {nome_arquivo}")
exportar_markdown_simples(df, "portarias-anac.md")

# Exporta para CSV
def exportar_csv(df, nome_arquivo):
    df.to_csv(nome_arquivo, index=False, quoting=csv.QUOTE_ALL)
    print(f"Arquivo CSV gerado com sucesso: {nome_arquivo}")
exportar_csv(df, "portarias-anac.csv")

# Exporta para TSV
def exportar_tsv(df, nome_arquivo):
    df.to_csv(nome_arquivo, sep='\t', index=False, quoting=csv.QUOTE_ALL)
    print(f"Arquivo TSV gerado com sucesso: {nome_arquivo}")
exportar_tsv(df, "portarias-anac.tsv")

# Exporta para JSON
def exportar_json(df, nome_arquivo):
    # Cria uma lista de dicionários
    dados_json = []
    for _, row in df.iterrows():
        linha_dict = {}
        for col in df.columns:
            valor = row[col]
            # Verifica se o valor contém links (mais de um link na célula)
            if isinstance(valor, str) and '(' in valor and ')' in valor:
                # Divide os links presentes na célula
                links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', valor)
                linha_dict[col] = [{'titulo': texto, 'url': url} for texto, url in links]
            else:
                linha_dict[col] = valor
        dados_json.append(linha_dict)
    # Salva o arquivo JSON
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados_json, f, ensure_ascii=False, indent=4)
    print(f"Arquivo JSON gerado com sucesso: {nome_arquivo}")
exportar_json(df, "portarias-anac.json")

# Exporta o arquivo em html
def exportar_html(df, nome_arquivo):
    df = df.apply(lambda col: col.apply(lambda x: " ".join([f'<a href="{u}">{t}</a>' for t, u in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', str(x))]) if isinstance(x, str) and '[' in x and '(' in x else x))
    html = df.to_html(index=False, escape=False)
    html = f'<meta charset="UTF-8">\n' + html
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(html)   
    print(f"Arquivo HTML gerado com sucesso: {nome_arquivo}")
exportar_html(df, "portarias-anac.html")