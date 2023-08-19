from random import randint
numeros_aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
print('Os valores sorteados foram:')
for c in numeros_aleatorios:
    print(f'{c} ', end='')

print(f'''\nO menor valor foi: {min(numeros_aleatorios)}
O maior valor foi: {max(numeros_aleatorios)}''')
