lista = []
lista_par = []
lista_impar = []
for c in range(0, 7):
    n = int(input(f'Digite o {c+1} valor: '))
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

lista_par.sort()
lista_impar.sort()
lista.append(lista_par)
lista.append(lista_impar)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
