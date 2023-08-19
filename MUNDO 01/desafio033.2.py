a = float(input('1º valor: '))
b = float(input('2º valor: '))
c = float(input('3º valor: '))

#verificando quem é menor
menor = a
if (b<a) and (b<c):
    menor = b
elif (c<a) and (c<b):
    menor = c
#verificando quem é maior
maior = a
if (b>a) and (b>c):
    maior = b
elif (c>a) and (c>b):
    maior = c

print('O menor valor digitiado foi: {}\n' 'O maior valor digitado foi: {}\n'.format(menor, maior))
