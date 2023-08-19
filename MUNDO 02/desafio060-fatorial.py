num = int(input('Para qual numero deseja calcular o seu fatorial? '))
fatorial = num
c = num

print('Calculando {}! = {} '.format(num, num), end='')
while c!=1:
    c -= 1
    fatorial *= c
    print('x {} '.format(c), end='')
print(' = {}'.format(fatorial))
