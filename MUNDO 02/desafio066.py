print('Irei ler todos numéros que você digitar, com exceção do num [999] que é a condição de parada.')
c = 0
soma = 0
while True:
    n = int(input('Digite um valor inteiro: '))
    if n == 999:
        break
    c += 1
    soma += n

print(f'Foram digitados {c} valores, cuja soma entre eles é igual a: {soma}')
