import boto3
import pandas as pd
from io import StringIO
from datetime import datetime

nome_bucket = 'desafioaws'

# informações do arquivo series
nome_arq_series = 'series.csv'
caminho_arq_local_series = 'series.csv'

# informações do arquivo movies
nome_arq_movies = 'movies.csv'
caminho_arq_local_movies = 'movies.csv'

# data para o caminho do arquivo
data_atual = datetime.now()

ano = data_atual.year
mes = data_atual.month
dia = data_atual.day

caminho_arq_s3 = 'Raw/Local/CSV/'

caminho_arq_s3_series = f'{caminho_arq_s3}Series/{ano}/{mes}/{dia}/series.csv'
caminho_arq_s3_movies = f'{caminho_arq_s3}Movies/{ano}/{mes}/{dia}/movies.csv'

# Leitura do arquivo CSV local usando o pandas
dfs = pd.read_csv(caminho_arq_local_series, sep="|", low_memory=False)
dfm = pd.read_csv(caminho_arq_local_movies, sep="|", low_memory=False)

# Upload da string CSV para o S3, incluindo o caminho do diretório e o nome do arquivo
s3 = boto3.client('s3')

# Carrega os dados de séries no S3
csv_buffer_series = StringIO()
dfs.to_csv(csv_buffer_series, index=False)
s3.put_object(Body=csv_buffer_series.getvalue(), Bucket=nome_bucket, Key=caminho_arq_s3_series)

# Carrega os dados de filmes no S3
csv_buffer_movies = StringIO()
dfm.to_csv(csv_buffer_movies, index=False)
s3.put_object(Body=csv_buffer_movies.getvalue(), Bucket=nome_bucket, Key=caminho_arq_s3_movies)

print(f'O arquivo {nome_arq_series} foi carregado com sucesso no bucket {nome_bucket}.')
print(f'O arquivo {nome_arq_movies} foi carregado com sucesso no bucket {nome_bucket}.')
