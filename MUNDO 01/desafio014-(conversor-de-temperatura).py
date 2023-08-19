#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Informe a temperatura em ºC: '))
conv = (temp*(9/5))+32

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF'.format(temp, conv)) #:.1f - precisao de 1 casa decimal

