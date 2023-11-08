import pandas as pd

banco = pd.read_csv("actors.csv")
ator = banco[banco['Number of Movies'] == max(banco['Number of Movies'])]
print(ator[['Actor','Number of Movies']])