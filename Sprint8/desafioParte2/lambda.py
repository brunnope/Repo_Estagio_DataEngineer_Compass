#código lambda

import json

def lambda_handler(event, context):
    import urllib.request
    import boto3
    from datetime import datetime
    from time import sleep
    import pandas as pd
    import os
    
    #esconde chave api e cria o cliente
    api_key = os.environ["api_key"]
    s3 = boto3.client('s3')
    dados = []
 
    #percorre todas as 150 páginas do meu filtro aplicado pelo gênero drama e romance de filmes brasileiros desde 2010
    for i in range(150):
        discover_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&include_adult=false&page={i+1}&primary_release_date.gte=2010-01-01&primary_release_date.lte=2023-12-31&with_genres=10749%7C18&with_original_language=pt"

        #sleep para respeitar o limite de chamada por segundo
        sleep(0.03)

        #pega os dados e armazena em dados que irá conter todos os filmes
        with urllib.request.urlopen(discover_url) as response:
            data = json.loads(response.read().decode('utf-8'))
            dados.extend(data['results'])

        #agrupar em arquivos de 100 filmes
        if (len(dados) == 100):
            dadosComImdb = []
            for i in dados:
                id = i['id']
                moviesDetails_url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}"
                sleep(0.06)
                
                with urllib.request.urlopen(moviesDetails_url) as response:
                    data = json.loads(response.read().decode('utf-8'))
                    dadosComImdb.append(data)

            #cria um data frame para específicar a leitura na tranformação para json 
            data_frameDadosComImdb = pd.DataFrame(dadosComImdb)
            data_frameDadosComImdbJson = data_frameDadosComImdb.to_json(orient="records")
    
            data_exec = datetime.now()
    
            ano = data_exec.year
            mes = data_exec.month
            dia = data_exec.day
            
            #se baseia na chamada do time para definir um nome específico para o arquivo
            nome_arq = f"{data_exec.minute}min-{data_exec.second}s-{data_exec.microsecond}ms"
            caminho_arq_json = f"Raw/tmdb/json/{ano}/{mes}/{dia}/{nome_arq}.json"

            #sobe para o s3 e limpa dados para receber os próximos 100 filmes
            s3.put_object(Body=data_frameDadosComImdbJson, Bucket="desafioaws", Key=caminho_arq_json)
            dados.clear()
            print(f"ARQUIVO {nome_arq} TRANSFERIDO COM SUCESSO! \n")
    
    #mensagem quando o lambda é finalizado com sucesso
    return {
        'statusCode': 200,
        'body': 'TODOS OS ARQUIVOS TRANSFERIDOS COM SUCESSO!'
    }
