#outro teste feito por mim

import requests
import pandas as pd
import os
from IPython.display import display

api_key = os.environ["api_key"]

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
