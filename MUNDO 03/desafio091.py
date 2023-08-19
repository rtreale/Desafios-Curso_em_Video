from random import randint
from time import sleep
from operator import itemgetter
jogos = dict()
for c in range(0, 4):
    jogos[f'jogador{c+1}'] = randint(1, 6)
#print(jogos) #dicionario
print('Valores sorteados:')
for k, v in jogos.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = dict()
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
#print(ranking) #virou uma lista
print('Ranking dos jogadores:')
for k, v in enumerate(ranking): #o comando de ordenamento de ranking torna essa variavel uma lista, por isso tive que colocar a exibição com enumerate
    print(f'{k+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
