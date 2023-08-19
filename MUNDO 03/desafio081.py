lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    requestion = ' '
    while requestion not in 'SN':
        requestion = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if requestion == 'N':
        break

lista_decrescente = lista[:]
lista_decrescente.sort(reverse=True)

print(f'a) Foram digitados {len(lista)} números.')
print(f'b) Valores ordenados de forma decrescente: {lista_decrescente}')
if 5 in lista:
    print('c) O valor 5 foi digitado e encontra-se na(s) posição(ões): ', end='')
    for v, c in enumerate(lista_decrescente):
        if c == 5:
            print(f'{v+1} |', end=' ')
else:
    print('c) O valor 5 não foi digitado.')