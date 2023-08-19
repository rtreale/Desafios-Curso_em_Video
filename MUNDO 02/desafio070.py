nome = str(input('Nome do produto: ')).strip()
preco = float(input('Preço do produto R$ '))

barato = preco
nome_barato = nome
total_compra = preco
mais_1000 = 0

while True:
    if preco<barato:
        barato = preco
        nome_barato = nome
    if preco>1000:
        mais_1000 += 1

    question = ' '
    while question not in 'SN':
        question = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if question == 'S':
        nome = str(input('Nome do produto: ')).strip()
        preco = float(input('Preço do produto R$ '))
        total_compra += preco
    elif question == 'N':
        break

print(f'''O total da compra foi R${total_compra:.2f}
Temos {mais_1000} produto(s) que custam mais de R$1000.00
O produto mais barato foi {nome_barato} que custa R${barato:.2f}''')