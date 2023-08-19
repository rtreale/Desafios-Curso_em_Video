from random import randint
from time import sleep #sleep faz o computador ter um delay antes de exibir a mensagem
randnum = int(randint(0,5))
usernum = int(input('Chute um numero entre 0 e 5: '))

print('PROCESSANDO...')
sleep(2) #faz o pc dar um delay antes de exibir a msng, o valor nos parenteses é o tempo do delay

if (usernum==randnum):
    print('Parabéns você acertou!!!')
else:
    print('Que pena você errou, o numero ao acaso era: {}'.format(randnum))
exit()