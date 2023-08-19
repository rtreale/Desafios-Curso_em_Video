lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    request = ' '
    while request not in 'SN':
        request = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if request == 'N':
        break

lista_par = lista[:]
lista_impar = lista[:]
for c in lista_par:
    if c % 2 != 0:
        lista_par.remove(c)
for c in lista_impar:
    if c % 2 == 0:
        lista_impar.remove(c)

print(f'''Lista entrada de dados: {lista}
Lista de numeros pares: {lista_par}
Lista de numeros ímpares: {lista_impar}''')
