contador = 0
soma = 0
print('Digite quantos numeros quiser ...\nOBS: O número [999] é a condição de parada do programa')
while True:
    n = int(input())
    if n == 999:
        break
    else:
        contador += 1
        soma += n
print(f'Foram digitados {contador} numeros, cuja soma entre eles é {soma}')
