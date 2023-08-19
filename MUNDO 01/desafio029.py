vel = float(input('Qual a velocidade do carro? '))

if (vel>80):
    multa = (vel-80)*7
    print('O carro foi multado em R${:.2f} pois ultrapassou em {}km/h a velocidade maxima permitida da via que é de 80km/h'.format(multa, multa/7))
else:
    exit()
exit()