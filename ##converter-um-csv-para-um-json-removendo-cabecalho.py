## converter arquivo csv para um arquivo json removendo cabecalho
import pandas as pd
import csv
import json

file = open('data.csv', 'r')    # abrir o arquivo
reader = csv.reader(file)       # ler o arquivo
df = list(reader)               # converter o arquivo para uma lista
df.pop(0)                       # remover o cabeçalho
df = [dict(zip(df[0], row)) for row in df] # converter a lista para um dicionário
df = json.dumps(df)            # converter o arquivo para json
df = json.loads(df)            # converter o arquivo para lista
df.to_json('data.json', indent=4) # salvar o arquivo json
file.close()                   # fechar o arquivo