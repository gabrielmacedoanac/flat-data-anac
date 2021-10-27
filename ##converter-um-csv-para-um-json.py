## converter um arquivo csv para um arquivo json
## usando o pandas
import pandas as pd
import csv
import json

def main():
    # caminho para o arquivo csv
    caminho = './csv/concatenado.csv'
    # carrega o arquivo
    dados = pd.read_csv(caminho)
    # converte o dataframe para json
    json_data = dados.to_json(orient='records')
    # salva o json
    with open('concatenado.json', 'w') as f:
        f.write(json_data)