print('Vou verificar se os segmentos de retas digitados por você formam um triangulo...')

r1 = float(input('1º reta: '))
r2 = float(input('2º reta: '))
r3 = float(input('3º reta: '))

if ((r1+r2)>r3) and ((r2+r3)>r1) and ((r1+r3)>r2):
    print('É possivel formar um triangulo com estes segmentos de retas!')
else:
    print('Não é possivel a existencia de um triangulo com estes segmentos de retas!')
exit()