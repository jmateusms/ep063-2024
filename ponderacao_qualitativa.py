# %% pacotes
import pandas as pd
import numpy as np

# %% dados
dados = pd.read_csv('localizacao/ex01.csv', header=0)

# %% aplicação do método
nomes = dados.columns.values[2:]
scores = []

for i in range(2, len(dados.columns)):
    scores.append(sum(dados['Peso'] * dados.iloc[:, i]))

# %% resultados
for nome, score in zip(nomes, scores):
    print(f'Instalação {nome}: {score}')

melhor_instalacao = np.argmax(scores)

print(f'\nMelhor instalação: {nomes[melhor_instalacao]}. Pontuação: {scores[melhor_instalacao]}')
