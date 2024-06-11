# %% pacotes
import numpy as np
import pandas as pd
from itertools import combinations, permutations
from tqdm import tqdm

# %% dados
# m = 3
# n = 2
n = 3
m = 4
w = 10
h = 5

# setores = ['0', '1', '2', '3', '4', '5']
setores = [str(i) for i in range(m * n)]
planta_atual = np.array(setores).reshape(n, m)

# planta = np.array(
#     [['0', '1', '2'],
#      ['3', '4', '5']]
# )

custos = pd.read_csv(f'funcional_dados/custos{n}x{m}.csv', header=0)
custos['origem'] = custos['origem'].astype(str)
custos.set_index('origem', inplace=True)
mov = pd.read_csv(f'funcional_dados/movimentacoes{n}x{m}.csv', header=0)
mov['origem'] = mov['origem'].astype(str)
mov.set_index('origem', inplace=True)

coordenadas = [(i, j) for i in range(n) for j in range(m)]
# coordenadas = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
# combinacoes = combinations(coordenadas, 2)

# %% funções
def dist_indireta(a, b):
    return h * abs(b[0] - a[0]) + w * abs(b[1] - a[1])


def dist_direta(a, b):
    return np.sqrt((h * (b[0] - a[0])) ** 2 + (w * (b[1] - a[1])) ** 2)


def calcular_distancias(planta):
    distancias_ind = pd.DataFrame(np.zeros((n * m, n * m)))
    distancias_ind.index = custos.index
    distancias_ind.columns = custos.columns
    distancias_dir = pd.DataFrame(np.zeros((n * m, n * m)))
    distancias_dir.index = custos.index
    distancias_dir.columns = custos.columns

    for c1, c2 in combinations(coordenadas, 2):
        setor_c1 = planta[c1]
        setor_c2 = planta[c2]

        distancias_ind.loc[setor_c1, setor_c2] = distancias_ind.loc[setor_c2, setor_c1] = dist_indireta(c1, c2)
        distancias_dir.loc[setor_c1, setor_c2] = distancias_dir.loc[setor_c2, setor_c1] = dist_direta(c1, c2)

    return distancias_ind, distancias_dir


# a, b = (0, 0), (1, 2)
# print(dist_indireta(a, b))
# print(dist_direta(a, b))

# %% cálculos
# distancias_ind, distancias_dir = calcular_distancias(planta_atual)

# %% métricas
# print(f'Distância total (indireta): {distancias_ind.values.sum()}')
# print(f'Distância total (direta): {distancias_dir.values.sum()}')
# print(f'Custo por movimentação (dist. indireta): {np.sum(distancias_ind.values * custos.values)}')
# print(f'Custo por movimentação (dist. direta): {np.sum(distancias_dir.values * custos.values)}')
# print(f'Custo total (dist. indireta): {np.sum(distancias_ind.values * custos.values * mov.values)}')
# print(f'Custo total (dist. direta): {np.sum(distancias_dir.values * custos.values * mov.values)}')

# %% solução exaustiva
permutacoes = permutations(setores, len(setores))

menor_custo = np.inf
melhor_planta = None

for p in tqdm(list(permutacoes)):
    planta_atual = np.array(p).reshape(n, m)
    distancias_ind, distancias_dir = calcular_distancias(planta_atual)

    custo_atual = np.sum(distancias_dir.values * custos.values * mov.values)

    if custo_atual < menor_custo:
        menor_custo = custo_atual
        melhor_planta = planta_atual

# %% resultado
print(f'Menor custo: {menor_custo}')
print(melhor_planta)
