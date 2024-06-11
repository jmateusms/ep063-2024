# %% pacotes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% dados
dados = pd.read_csv('localizacao/ex02.csv', header=0)

# %% funções
def lucro(q, CF, CV, PV):
    return -CF + q * (PV - CV)


# %% ponto de equilíbrio
ponto_eq = np.ceil(dados['Custos fixos'] / (dados['Preço de venda'] - dados['Custo variável']))
ponto_eq = np.array(ponto_eq, dtype=int)

dados['Ponto de equilíbrio'] = ponto_eq

# %% lucros
qtds = [3000, 4000, 6000]

for q in qtds:
    lucros = []

    for i, linha in dados.iterrows():
        lucros.append(lucro(q, linha['Custos fixos'], linha['Custo variável'], linha['Preço de venda']))

    dados[f'Lucro ({q})'] = lucros
    melhor_i = np.argmax(lucros)
    print(f'Melhor lucro (q = {q}): {dados["Localização"][melhor_i]}, com lucro {dados[f"Lucro ({q})"][melhor_i]}')

# %% ranking
# dados.sort_values(by='Lucro (3000)', ascending=False)

# %% plot
for i, linha in dados.iterrows():
    plt.plot(qtds, linha.loc['Lucro (3000)':])
plt.show()
