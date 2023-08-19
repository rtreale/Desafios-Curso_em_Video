a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
c = 0
while c<10:
    print(f'{c+1:2}º termo = {a+r*c}')
    c += 1

fim = False
while not fim:
    continuar = str(input('Deseja mostrar mais alguns termos? [S/N] ')).strip().upper()
    if continuar == 'S':
        termos = int(input('Quantos temos a mais deseja exibir? '))
        contador = c+termos
        while c<contador:
            print(f'{c+1:2}º termo = {a + r * c}')
            c += 1
    elif continuar == 'N':
        fim = True
        print('O programa foi finalizado.')
    else:
        print('Opção inválida, escolha novamente.')
