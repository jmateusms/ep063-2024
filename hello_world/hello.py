import pandas as pd

notas = pd.read_csv('notas.csv', header=0)

def calc_media(n1, n2):
    return (n1 + n2) / 2


# calc_media = lambda n1, n2 : (n1 + n2) / 2
# notas = [(9, 7), (10, 8), (7, 10), (9, 8.5), (3.5, 2), (2.5, 5.7)]

for i, aluno in notas.iterrows():
    media = calc_media(aluno['nota1'], aluno['nota2'])

    if media >= 7:
        print(f'{aluno["nome"]} aprovado(a) com média {media:.2f}')
    elif media >= 3:
        print(f'{aluno["nome"]} está na final com média {media:.2f}, precisando de {10-media:.2f}')
    else:
        print(f'{aluno["nome"]} reprovado(a) com média {media:.2f}')
