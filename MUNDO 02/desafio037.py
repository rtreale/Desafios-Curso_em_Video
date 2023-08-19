num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
 [ 1 ] converter para BINÁRIO
 [ 2 ] converter para OCTAL
 [ 3 ] converter para HEXADECIMAL''') #ao utilizar as 3 aspas posso dar a quebra de linha com enter e o programa entende
cond = int(input('Sua opção: '))

if cond == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif cond == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif cond == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')

#ao fim da conversao fatiamos a exibição para exibir a partir da 2º casa, para retirar as citações de bin, oct, e hx do python (0b = bin / 0o = oct / 0x = hex)
