from datetime import date
maior = 0
menor = 0
ano_atual = date.today().year

for c in range(0, 7):
    entrada = int(input('Digite o ano de nascimento: '))
    if (ano_atual-entrada)>=21:
        maior += 1
    else:
        menor += 1

print(f'De acordo com os dados {maior} atingiram a maioridade, enquanto que {menor} ainda são menores de idade.')