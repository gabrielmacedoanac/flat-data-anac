import asyncio
import aiohttp
import pandas as pd
from pandas.io.formats.style import Styler
import re
from bs4 import BeautifulSoup
import os
import json

# Prefixo de URL a ser buscada
prefixo_url = "https://www.anac.gov.br/assuntos/legislacao/legislacao-1/portarias/"
anos = range(2024, 1970, -1)

# Lista para armazenar os dados das tabelas
dados_tabela = []
urls_acessadas = set()

# Define a expressão regular para caracteres não imprimíveis
regex_nao_imprimiveis = re.compile(r'[\x00-\x1F\x7F]')

# Função para extrair dados da tabela HTML
def extrair_dados_tabela(tabela, ano):
    cabecalho = [th.get_text(strip=True) for th in tabela.find_all("th")]
    if ano == 2020:
        cabecalho[1], cabecalho[2] = cabecalho[2], cabecalho[1]

    if not dados_tabela:
        dados_tabela.append(cabecalho)

    linhas = tabela.find_all("tr")
    for linha in linhas:
        colunas = linha.find_all(["th", "td"])
        valores = []
        for coluna in colunas:
            links = coluna.find_all("a")
            if links:
                texto_links = [f"[{link.get_text(strip=True)}]({link['href']})" for link in links]
                valor = " ".join(texto_links)
            else:
                valor = coluna.get_text(strip=True)
            valor = regex_nao_imprimiveis.sub(" ", str(valor)).replace("|", " ").replace("  ", " ").strip()
            valores.append(valor)

        if not valores or valores == cabecalho:
            continue
        if ano == 2020:
            valores[1], valores[2] = valores[2], valores[1]
        dados_tabela.append(valores)

# Função assíncrona para acessar a URL e extrair dados
async def acessar_url(session, ano):
    url = f"{prefixo_url}{ano}"
    if url in urls_acessadas:
        return
    urls_acessadas.add(url)
    async with session.get(url) as response:
        if response.status != 200:
            return
        soup = BeautifulSoup(await response.text(), "html.parser")
        tabela = soup.find("table", {"id": "tabela-normas"})
        if tabela:
            extrair_dados_tabela(tabela, ano)

async def fetch_all():
    async with aiohttp.ClientSession() as session:
        tasks = [acessar_url(session, ano) for ano in anos]
        await asyncio.gather(*tasks)

if not asyncio.get_event_loop().is_running():
    asyncio.run(fetch_all())

# Cria um DataFrame do Pandas a partir dos dados extraídos
if dados_tabela:
    cabecalho = ["Norma", "Publicação", "Ementa", "Arquivo"]
    df = pd.DataFrame(dados_tabela[1:], columns=cabecalho)
    df = df.dropna(how='all').drop_duplicates()
    def extrair_data(valor):
        match = re.search(r'(\d{2}/\d{2}/\d{4})', str(valor))
        return match.group(0) if match else None
    df['Data'] = df['Norma'].apply(extrair_data)
    df.loc[pd.isna(df['Data']), 'Data'] = df.loc[pd.isna(df['Data']), 'Publicação'].apply(extrair_data)
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce').dt.strftime('%Y-%m-%d')
    df = df[~((df['Norma'] == 'Norma') & (df['Publicação'] == 'Data') & (df['Ementa'] == 'Ementa') & (df['Arquivo'] == 'Arquivo'))]
    def formatar_data(x):
        try:
            return pd.to_datetime(x, format='%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            print(f"Erro ao formatar a data: {x}")
            return pd.NaT

    df['Data'] = df['Data'].mask(
        pd.isna(df['Data']),
        df['Publicação'].str.extract(r'(\d{2}/\d{2}/\d{4})', expand=False).apply(formatar_data)
    )    
    cols = ['Data'] + [col for col in df.columns if col != 'Data']
    df = df[cols]
    df = df.sort_values(by=['Data', 'Norma'], ascending=[False, False])

    # Exporta para Markdown
    def exportar_markdown_simples(df, nome_arquivo):
        linhas = ["| " + " | ".join(df.columns) + " |"]
        linhas.append("| " + " | ".join(["---"] * len(df.columns)) + " |")
        for _, row in df.iterrows():
            linha_formatada = [regex_nao_imprimiveis.sub(" ", str(valor)).replace("|", " ").replace("  ", " ") for valor in row.values]
            linhas.append("| " + " | ".join(linha_formatada) + " |")
        with open(nome_arquivo, "w") as f:
            f.write("\n".join(linhas))

    exportar_markdown_simples(df, "portarias-anac.md")

    # Exporta para CSV
    def exportar_csv(df, nome_arquivo):
        df.to_csv(nome_arquivo, index=False)
        print(f"Arquivo CSV gerado com sucesso: {nome_arquivo}")

    exportar_csv(df, "portarias-anac.csv")

    # Exporta para TSV
    def exportar_tsv(df, nome_arquivo):
        df.to_csv(nome_arquivo, sep='\t', index=False)
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


    # Salva o arquivo em html
    def exportar_html(df, nome_arquivo):
        # Cria uma cópia do DataFrame para evitar modificações diretas no original
        df_copy = df.copy()

        # Função para formatar células com links
        def formatar_links(celula):
            # Se houver múltiplos links, separa-os e adiciona o título de cada link
            if isinstance(celula, str) and '[' in celula and ']' in celula and '(' in celula and ')' in celula:
                # Identifica os links no formato Markdown
                links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', celula)
                # Formata cada link no formato HTML <a href="URL">Título</a>
                return " ".join([f'<a href="{url}">{titulo}</a>' for titulo, url in links])
            return celula

        # Aplica a formatação de links a todo o DataFrame
        df_copy = df_copy.applymap(formatar_links)

        # Converte o DataFrame para HTML
        html = df_copy.to_html(index=False, escape=False)

        # Salva o HTML em um arquivo
        with open(nome_arquivo, "w") as f:
            f.write(html)

        print(f"Arquivo HTML gerado com sucesso: {nome_arquivo}")

    # Exemplo de uso
    exportar_html(df, "portarias-anac.html")

else:
    print("Nenhuma tabela foi extraída.")
