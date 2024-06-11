# %% pacotes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% dados
dados = pd.read_csv('localizacao/ex05.csv')

# %% preparação dos dados
dados_x = dados.sort_values(by='X', ascending=True)
dados_y = dados.sort_values(by='Y', ascending=True)

med1 = dados['Volume'].sum() / 2
if med1 % 2:
    med2 = med1 + 1
else:
    med2 = med1

# %% X
dados_x['Soma'] = dados_x['Volume'].cumsum()
flag1 = flag2 = False
X1 = X2 = 0

for i, linha in dados_x.iterrows():
    if linha['Soma'] >= med1 and not flag1:
        X1 = linha['X']
        flag1 = True
    if linha['Soma'] >= med2 and not flag2:
        X2 = linha['X']
        flag2 = True
    if flag1 and flag2:
        break

# %% Y
dados_y['Soma'] = dados_y['Volume'].cumsum()
flag1 = flag2 = False
Y1 = Y2 = 0

for i, linha in dados_y.iterrows():
    if linha['Soma'] >= med1 and not flag1:
        Y1 = linha['Y']
        flag1 = True
    if linha['Soma'] >= med2 and not flag2:
        Y2 = linha['Y']
        flag2 = True
    if flag1 and flag2:
        break

# %% resultados
print(f'X1 = {X1}, X2 = {X2}')
print(f'Y1 = {Y1}, Y2 = {Y2}')

plt.scatter(dados['X'], dados['Y'], color='tab:blue')
for i, linha in dados.iterrows():
    plt.annotate(linha['Localização'][-1:], xy=(linha['X'], linha['Y']), xytext=(1.02*linha['X'], 1.02*linha['Y']))
plt.scatter(X1, Y1, color='tab:red')
plt.annotate(f'Med ({X1:.2f}, {Y1:.2f})', (X1, Y1), xytext=(X1*1.02, Y1*1.02))
if X1 != X2:
    plt.scatter(X2, Y1, color='tab:red')
    plt.annotate(f'Med ({X2:.2f}, {Y1:.2f})', (X2, Y1), xytext=(X2 * 1.02, Y1 * 1.02))
    if Y1 != Y2:
        plt.scatter(X2, Y2, color='tab:red')
        plt.annotate(f'Med ({X2:.2f}, {Y2:.2f})', (X2, Y2), xytext=(X2 * 1.02, Y2 * 1.02))
if Y1 != Y2:
    plt.scatter(X1, Y2, color='tab:red')
    plt.annotate(f'Med ({X1:.2f}, {Y2:.2f})', (X1, Y2), xytext=(X1 * 1.02, Y2 * 1.02))
plt.xlim((0, 200))
plt.ylim((0, 200))

X = np.sum(dados['Volume'] * dados['X']) / np.sum(dados['Volume'])
Y = np.sum(dados['Volume'] * dados['Y']) / np.sum(dados['Volume'])
plt.scatter(X, Y, color='tab:orange')
plt.annotate(f'CG ({X:.2f}, {Y:.2f})', xy=(X, Y), xytext=(1.02*X, 1.02*Y))

plt.show()
