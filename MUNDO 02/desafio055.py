maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Qual o peso do {c}º paciente? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso>maior:
            maior = peso
        if peso<menor:
            menor = peso

print(f'O maior peso: {maior:.2f} [kg]\nO menor peso: {menor:.2f} [kg]')