lista = []
for c in range(0, 5):
    n = int(input(f'Digite o {c+1}º numero: '))
    if (c == 0) or n > lista[-1]: #lista[-1] = lista[len(lista)-1] = ultimo elemento da lista
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'Valores em ordem crescente na lista: {lista}')