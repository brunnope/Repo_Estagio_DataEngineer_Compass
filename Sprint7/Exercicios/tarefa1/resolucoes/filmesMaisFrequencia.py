import pandas as pd

filmes = pd.read_csv("actors.csv")['#1 Movie']
print(filmes.value_counts())