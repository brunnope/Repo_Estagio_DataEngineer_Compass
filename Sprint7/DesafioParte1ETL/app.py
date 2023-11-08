import boto3
import pandas as pd
from io import StringIO

# informações bucket
nome_bucket = 'desafioaws'
nome_arq = 'series.csv'
caminho_arq_local = 'series.csv'

# Leitura do arquivo CSV local usando o pandas
df = pd.read_csv(caminho_arq_local, sep="|", low_memory=False)

csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

# Faz o upload da string CSV para o S3
s3 = boto3.client('s3')
s3.put_object(Body=csv_buffer.getvalue(), Bucket=nome_bucket, Key=nome_arq)

print(f'O arquivo {nome_arq} foi carregado com sucesso no bucket {nome_bucket}.')
