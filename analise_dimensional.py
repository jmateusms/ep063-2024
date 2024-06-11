# %% pacotes
import pandas as pd
import numpy as np
from itertools import combinations

# %% dados
dados = pd.read_csv('localizacao/ex03.csv', header=0)
nomes = dados.columns[2:]

# %%
pares = list(combinations(nomes, 2))
CMs = []
scores = {
    'A': 0,
    'B': 0,
    'C': 0
}

for i1, i2 in pares:
    cm = np.prod((dados[i1] / dados[i2]) ** dados['Peso'])
    CMs.append(cm)
    if cm < 1:
        scores[i1] += 1
    elif cm > 1:
        scores[i2] += 1
    else:
        scores[i1] += 1
        scores[i2] += 1

for par, cm in zip(pares, CMs):
    print(f'{par[0]} vs {par[1]}: {cm:.3f}')

print(scores)