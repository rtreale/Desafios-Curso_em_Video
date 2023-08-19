camp = dict()
gols = list()
tot = 0
camp['nome'] = str(input('Nome do Jogador: ')).strip()
n = int(input(f'Quantas partidas {camp["nome"]} jogou? '))
for c in range(0, n):
    gol = int(input(f'Quantos gols na partida {c+1}? '))
    tot += gol
    gols.append(gol)
camp['gols'] = gols[:]
camp['total'] = tot
print(f'{"-="*30}\n{camp}\n{"-="*30}')
print(f'O jogador {camp["nome"]} jogou {n} partidas.')
for c in range(0, n):
    print(f'    => Na partida {c+1}, fez {camp["gols"][c]} ')
print(f'Foi um total de {camp["total"]} gols.')
