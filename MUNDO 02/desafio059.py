fim = False
while not fim:
    print('Digite 2 valores: ')
    a = float(input('Primeiro valor: '))
    b = float(input('Segundo valor: '))
    menu = int(input('''Qual operação deseja realizar?\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\n'''))
    if menu == 1:
        print('A soma entre {} e {} é igual a: {}'.format(a, b, a+b))
    elif menu == 2:
        print('A multiplicação entre {} e {} é igual a: {}'.format(a, b, a*b))
    elif menu == 3:
        if a>b:
            print('O maior valor entre {} e {} é: {}'.format(a, b, a))
        elif b>a:
            print('O maior valor entre {} e {} é: {}'.format(a, b, b))
        elif a==b:
            print('Os valores sao iguais.')
    elif menu == 4:
        print('Entre com novos dados:')
    elif menu == 5:
        fim = True
    else:
        print('Opção inválida, escolha um numero exibido no menu.')
