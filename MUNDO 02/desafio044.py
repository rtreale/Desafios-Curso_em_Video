print('{:=^40}'.format(' LOJA VIRTUAL ')) #o sinal de (^) centraliza a mensagem loja virtual entre 40 sinais de (=)
preco_prod = float(input('Qual o valor das compras? R$'))
print('''Defina a condição de pagamento:
[ 1 ] À vista no dinheiro/cheque: 10% de desconto.
[ 2 ] À vista no cartão: 5% de desconto.
[ 3 ] 2x no cartão: preço normal.
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opcao = int(input('Opção escolhida: '))

if opcao == 1:
    print('Preço final do produto: R$', end='')
    print(f'{preco_prod*0.90:.2f}')
elif opcao == 2:
    print('Preço final do produto: R$', end='')
    print(f'{preco_prod*0.95:.2f}')
elif opcao == 3:
    print(f'Sua compra será parcelada em 2x de R${(preco_prod/2):.2f}')
    print('Preço final do produto: R$', end='')
    print(f'{preco_prod:.2f}')
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas irá dividir? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${((preco_prod*1.20)/parcelas):.2f}')
    print('Preço final do produto: R$', end='')
    print(f'{preco_prod*1.20:.2f}')
else:
    print('Opções de pagamento invalidas, tente novamente.')
