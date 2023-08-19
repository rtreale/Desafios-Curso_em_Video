from random import randint
palpite_pc = randint(0, 10)

print('Pensei em um numero entre 0 e 10, duvido você acertar!')

palpites = 0
acertou = False

while not acertou:
    palpite_user = int(input('Qual é o seu palpite: '))
    palpites += 1
    if palpite_user == palpite_pc:
        acertou = True
    else:
        if palpite_user>palpite_pc:
            print('Dica: chute pra menos...')
        else:
            print('Dica: chute pra mais...')

print('''Parabéns você acertou depois de {} tentativas!!!
Palpite do pc: {}
Palpite do usuario: {}'''.format(palpites, palpite_pc, palpite_user))
