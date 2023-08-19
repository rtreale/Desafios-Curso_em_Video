dist = float(input('Qual a distancia da viagem? '))

if (dist <= 200):
    print('Cota 01 aplicada \n' 'Valor da passagem: R${:.2f}'.format(dist*0.50))
else:
    print('Cota 02 aplicada \n' 'Valor da passagem: R${:.2f}'.format(dist*0.45))
exit()