print('-'*50)
print('{:=^50}'.format(' Sequencia de Fibonacci '))
#print('Sequencia de Fibonacci')
print('-'*50)

n = int(input('Quantos termos deseja analisar? '))
fim = 2
fibo0 = 0
fibo1 = 1

if n == 0:
    exit(0)
elif n == 1:
    print(f'{fibo0}')
elif n == 2:
    print(f'{fibo0} -> {fibo1}', end='')
else:
    print(f'{fibo0} -> {fibo1}', end='')
    while fim<n:
        fibo = fibo0+fibo1
        print(f' -> {fibo}', end='')
        fibo0 = fibo1
        fibo1 = fibo
        fim +=1
print(' -> FIM!')
