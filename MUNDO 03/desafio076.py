listagem = ('Lápis', 1.75, 'Borracha',  2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Moochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print(f'{"-"*40}\n{"LISTAGEM DE PREÇOS":^40}\n{"-"*40}')
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<30}R${listagem[c+1]:7.2f}')
print(f'{"-"*40}')