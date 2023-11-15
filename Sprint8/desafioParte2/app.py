import json
import urllib.request
import boto3
from datetime import datetime
from time import sleep
import pandas as pd

data_atual = datetime.now()

ano = data_atual.year
mes = data_atual.month
dia = data_atual.day

api_key = "e3cd69f0bfe2927b56b7999439667b6e"
s3 = boto3.client('s3')
dados = []


for i in range(150):
    discover_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&include_adult=false&page={i+1}&primary_release_date.gte=2010-01-01&primary_release_date.lte=2023-12-31&with_genres=10749%7C18&with_original_language=pt"

    sleep(0.03)
    with urllib.request.urlopen(discover_url) as response:
        data = json.loads(response.read().decode('utf-8'))
        dados.extend(data['results'])

    if (len(dados) == 100):
        dadosComImdb = []
        for i in dados:
            id = i['id']
            moviesDetails_url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}"
            sleep(0.06)
            
            with urllib.request.urlopen(moviesDetails_url) as response:
                data = json.loads(response.read().decode('utf-8'))
                dadosComImdb.append(data)
            
        data_frameDadosComImdb = pd.DataFrame(dadosComImdb)
        data_frameDadosComImdbJson = data_frameDadosComImdb.to_json(orient="records")

        horario = datetime.now()
        nome_arq = f"{horario.minute}min-{horario.second}s-{horario.microsecond}ms"
        caminho_arq_json = f"Raw/tmdb/json/{ano}/{mes}/{dia}/{nome_arq}.json"

        s3.put_object(Body=data_frameDadosComImdbJson, Bucket="desafioaws", Key=caminho_arq_json)
        dados.clear()
        print(f"ARQUIVO {nome_arq} TRANSFERIDO COM SUCESSO! \n")


