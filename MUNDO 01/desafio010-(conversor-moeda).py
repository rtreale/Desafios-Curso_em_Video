real = float(input('Digite quantos reais deseja converter: '))
dolar = 3.27
conversao = real*dolar

print('R${} equivale à ${:.2f}'.format(real, conversao))
