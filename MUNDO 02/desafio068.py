from random import randint
vitorias_user = 0
while True:
    pc = randint(0,10)
    par_impar = ' '
    while par_impar not in 'PI': #essa verificação é para o usuario nao digitar valores diferentes de P ou I
        par_impar = str(input('Escolha entre par ou ímpar [P/I] ')).strip().upper()[0]
    user = int(input('Digite um valor entre 0 e 10: '))
    resultado = pc+user
    print(f'Apurador de valores: [PC: {pc} / USER: {user}]')
    if (par_impar == 'PAR') and (resultado%2==0):
        vitorias_user += 1
        print('Você ganhou!!!')
    elif (par_impar == 'IMPAR') and (resultado%2!=0):
        vitorias_user += 1
        print('Você ganhou!!!')
    else:
        print('A máquina ganhou!!! Fim do programa.')
        break
print(f'Você obteve {vitorias_user} vitória(s)')