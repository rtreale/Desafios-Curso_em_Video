prod = float(input('Digite o preço do produto: '))
desc = prod*0.95

print('O produto que custava R${:.2f}, passou a custar R${:.2f}, dado os 5% de desconto da compra à vista'.format(prod, desc))
