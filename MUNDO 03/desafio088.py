from random import randint
from time import sleep
lista_jogos = []
dados = []
print(f'{"-"*40}\n{"GERADOR DE JOGOS":^40}\n{"-"*40}')
n = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, n):
    for c in range(0, 6):
        x = randint(1, 60)
        while x in dados:
            x = randint(1, 60)
            if x not in dados:
                break
        dados.append(x)
    dados.sort()
    lista_jogos.append(dados[:])
    dados.clear()

print('-'*10 ,f'SORTEANDO {n} JOGOS', '-'*11)
for c in range(0, len(lista_jogos)):
    print(f'Jogo {c+1}: {lista_jogos[c]}')
    sleep(0.8)