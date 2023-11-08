import pandas as pd
import numpy as np

Numfilmes = pd.read_csv("actors.csv")['Number of Movies']
media = np.average(Numfilmes.array)

print(f'Media: {media:.2f}')