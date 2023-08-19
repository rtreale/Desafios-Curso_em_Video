print('Digite 3 numeros para análise: ')
a = float(input('1º num: '))
b = float(input('2º num: '))
c = float(input('3º num: '))

if ((a>b) and (a>c)) and (c>b):
    print('Maior num: {}\n' 'Menor num: {}\n'.format(a, b))
elif ((a>b) and (a>c)) and (b>c):
    print('Maior num: {}\n' 'Menor num: {}\n'.format(a, c))
elif ((b>a) and (b>c)) and (c>a):
    print('Maior num: {}\n' 'Menor num: {}\n'.format(b, a))
elif ((b>a) and (b>c)) and (a>c):
    print('Maior num: {}\n' 'Menor num: {}\n'.format(b, c))
elif ((c>a) and (c>b)) and (b>a):
    print('Maior num: {}\n' 'Menor num: {}\n'.format(c, a))
else:
    print('Maior num: {}\n' 'Menor num: {}\n'.format(c, b))
