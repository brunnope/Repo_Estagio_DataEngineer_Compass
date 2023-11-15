import requests
import pandas as pd

from IPython.display import display

api_key = "e3cd69f0bfe2927b56b7999439667b6e"

url = f"https://api.themoviedb.org/3/movie/157336?api_key={api_key}"

response = requests.get(url)
data = response.json()
interestelar = []
dados = {'Título': data["original_title"],
                'Idioma': data["original_language"],
                'Votos': data['vote_average']
}

interestelar.append(dados)
print(interestelar)
dataFrameInter = pd.DataFrame(interestelar)
display(dataFrameInter)

"""
filmes = []

for movie in data['results']:
    df = {'Titulo': movie['title'],
    'Data de lançamento': movie['release_date'],
    'Visão geral': movie['overview'],
    'Votos': movie['vote_count'],
    'Média de votos:': movie['vote_average']}
    filmes.append(df)

df = pd.DataFrame(filmes)
display(df)"""