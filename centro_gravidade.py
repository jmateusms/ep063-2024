# %% pacotes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% dados
dados = pd.read_csv('localizacao/ex04.csv')

# %% CG
X = np.sum(dados['Volume'] * dados['X']) / np.sum(dados['Volume'])
Y = np.sum(dados['Volume'] * dados['Y']) / np.sum(dados['Volume'])

print(f'Centro de gravidade: ({X:.2f}, {Y:.2f})')

# %% plot
plt.scatter(dados['X'], dados['Y'], color='tab:blue')
plt.scatter(X, Y, color='tab:red')
plt.xlim((0, 150))
plt.ylim((0, 150))
plt.show()
