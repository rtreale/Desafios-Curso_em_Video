matriz = [[], [], []]
soma_par = 0
soma_3coluna = 0
for c in range(0, 3):
    for v in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {v}]: '))
        matriz[c].append(n)
        if n % 2 == 0:
            soma_par += n
        if v == 2:
            soma_3coluna += n

print('*='*30)
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[ {matriz[c][v]:^5} ]', end='') #^5 = 5 espacos centralizados
    print()
print('*='*30)

print(f'A soma dos valores pares é: {soma_par}')
print(f'A soma dos valores da terceira coluna é: {soma_3coluna}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
