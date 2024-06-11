# %% pacotes
import numpy as np
import pandas as pd

# %% dados
dados = pd.read_csv('dijkstra/ex01.csv', header=None)

# %% inicialização
nos = list(dados.index)
visitados = len(dados) * [False]
dists = [0] + (len(dados) - 1) * [np.inf]
rotas = [[0]] + (len(dados) - 1) * [[]]
corrente = 0
print(f'Nó {corrente} selecionado como nó corrente.')

# %% dijkstra
while corrente is not None:
    vizinhos = []
    isna = dados.iloc[corrente].isna()
    for no in nos:
        if not visitados[no] and not isna[no]:
            vizinhos.append(no)

    print(f'Nó {corrente} tem vizinhos: {vizinhos}.')

    for no in vizinhos:
        if dists[corrente] + dados.iloc[corrente, no] < dists[no]:
            dists[no] = dists[corrente] + dados.iloc[corrente, no]
            rotas[no] = rotas[corrente] + [no]
            print(f'Rota com distância {dists[no]} encontrada para o nó {no}.')

    visitados[corrente] = True
    print(f'Nó {corrente} marcado como visitado.')

    restantes = []
    dists_restantes = []
    for no in nos:
        if not visitados[no]:
            restantes.append(no)
            dists_restantes.append(dists[no])

    if len(restantes) > 0:
        if min(dists_restantes) == np.inf:
            corrente = None
            print('Não há mais caminhos possíveis.')
        else:
            corrente = restantes[np.argmin(dists_restantes)]
            print(f'Nó {corrente} selecionado como nó corrente.')
    else:
        corrente = None
        print('Todos os nós foram visitados.')

# %% imprimir resultados
print(f'Menores distâncias: {dists}')
print(f'Rotas: {rotas}')
