lista_master = []
dados = []
maior_peso = 0
menor_peso = 0
c = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista_master.append(dados[:])

    if c == 0:
        maior_peso = dados[1]
        menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        elif dados[1] < menor_peso:
            menor_peso = dados[1]

    dados.clear()
    c += 1

    request = ' '
    while request not in 'SN':
        request = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if request == 'N':
        break

print(f'Dados cadastrados: {lista_master}')
print(f'Ao todo você cadastrou {len(lista_master)} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for p in lista_master:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for p in lista_master:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')
