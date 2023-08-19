matriz = [[], [], []]
for c in range(0, 3):
    for v in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {v}]: ')))
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[ {matriz[c][v]:^5} ]', end='') #^5 = 5 espacos centralizados
    print()
