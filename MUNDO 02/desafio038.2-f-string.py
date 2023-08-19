x1 = int(input('Digite um valor inteiro: '))
x2 = int(input('Digite outro valor inteiro: '))

if x1>x2:
    print(f'{x1} é maior que {x2}, logo o primeiro valor é maior.')
elif x2>x1:
    print(f'{x2} é maior que {x1}, logo o segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
