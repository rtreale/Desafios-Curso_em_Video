soma = 0
for c in range(1,7):
    entrada = int(input(f'Digite {c}º valor inteiro: '))
    if (entrada%2 == 0):
        soma += entrada
print(f'A soma dos valores digitados que são pares é {soma}!')
