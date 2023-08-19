valores = []
for c in range(0, 5):
    valores.append(float(input(f'Digite o {c+1}º valor: ')))
print(f'''Os valores digitados foram: {valores}
Maior valor: {max(valores)}
Menor valor: {min(valores)}''')

print('O maior valor foi digitado na(s) posição(ões):', end='')
for v, c in enumerate(valores):
    if c == max(valores):
        print(f' {v+1} |', end='')
print() #quebra de linha
print('O menor valor foi digitado na(s) posição(ões):', end='')
for v, c in enumerate(valores):
    if c == min(valores):
        print(f' {v+1} |', end='')
