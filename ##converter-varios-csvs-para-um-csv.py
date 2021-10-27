## Converter vários arquivos csvs para um único arquivo csv 
## usando o pandas
import pandas as pd
import glob
import os

def main():
    # caminho para o diretório onde estão os arquivos
    caminho = './csv'
    # lista com os arquivos que serão convertidos
    arquivos = glob.glob(os.path.join(caminho, '*.csv'))
    # cria um dataframe vazio
    df = pd.DataFrame()
    # para cada arquivo na lista
    for arquivo in arquivos:
        # carrega o arquivo
        dados = pd.read_csv(arquivo)
        # adiciona os dados ao dataframe
        df = df.append(dados)
    # salva o dataframe como um arquivo csv
    df.to_csv('concatenado.csv')