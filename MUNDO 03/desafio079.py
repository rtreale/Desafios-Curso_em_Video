lista = []
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso!')

    requestion = ' '
    while requestion not in 'SN':
        requestion = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if requestion == 'N':
        break

print(f'Os valores digitados serão exibidos em ordem crescente: {sorted(lista)}')
