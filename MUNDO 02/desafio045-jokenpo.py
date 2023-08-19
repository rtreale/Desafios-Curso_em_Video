from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
user = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print(f'''{'-='*13}
O computador jogou {itens[pc]}
O jogador jogou {itens[user]}
{'-='*13}''')

print('RESULTADO: ', end='')
if pc == 0: #pc jogou pedra
    if user == 0:  # usuario jogou pedra
        print('EMPATE')
    elif user == 1:  # usuario jogou papel
        print('JOGADOR VENCE')
    elif user == 2:  # usuario jogou tesoura
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif pc == 1: #pc jogou papel
    if user == 0: #usuario jogou pedra
        print('COMPUTADOR VENCE')
    elif user == 1: #usuario jogou papel
        print('EMPATE')
    elif user == 2: #usuario jogou tesoura
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif pc == 2: #pc jogou tesoura
    if user == 0:  # usuario jogou pedra
        print('JOGADOR VENCE')
    elif user == 1:  # usuario jogou papel
        print('COMPUTADOR VENCE')
    elif user == 2:  # usuario jogou tesoura
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
