import pandas as pd

banco = pd.read_csv("actors.csv")
ator = banco[banco['Average per Movie'] == max(banco['Average per Movie'])]
print(ator.head())