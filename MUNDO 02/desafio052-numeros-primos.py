num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if (num%c==0):
        cont += 1
        print('\033[34m', end='') #cor azul - divisivel
    else:
        print('\033[31m', end='') #cor vermelha - não divisivel
    print(f'{c}\033[m', end=' ')

print(f'\nO número {num} foi divisível {cont} vezes.')

if (cont == 2):
    print('Desta forma é um numero primo!')
else:
    print('Desta forma não é um número primo')