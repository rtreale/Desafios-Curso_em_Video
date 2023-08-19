x1 = int(input('Digite um valor inteiro: '))
x2 = int(input('Digite outro valor inteiro: '))

if x1>x2:
    print('{} é maior que {}, logo o primeiro valor é maior.'.format(x1, x2))
elif x2>x1:
    print('{} é maior que {}, logo o segundo valor é maior.'.format(x2, x1))
else:
    print('Não existe valor maior, os dois são iguais.')
