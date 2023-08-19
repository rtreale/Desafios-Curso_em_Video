n = int(input('Digite um número: '))
maior = n
menor = n
media = n
cont = 1
while True:
    cond = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cond == 'N':
        break
    elif cond == 'S':
        n = int(input('Digite um número: '))
        if n>maior:
            maior = n
        elif n<menor:
            menor = n
        media += n
        cont += 1
    else:
        print('Opção inválida, tente novamente.')

print('Temos como resultado, o menor valor {}, o maior valor {}, a média dos {} valores digitados igual a {:.1f}'.format(menor, maior, cont, media/cont))
