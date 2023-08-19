maior_18 = 0
homens = 0
mulheres_menor20 = 0

while True:
    print('Registro de usuário:')
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in 'MF': #essa verificação é para o usuario nao digitar valores diferentes de M ou F
        sexo = str(input('Qual sexo? [M/F] ')).strip().upper()[0]

    if sexo == 'M':
        homens += 1
    if idade>18:
        maior_18 += 1
    if (sexo == 'F') and (idade < 20):
        mulheres_menor20 += 1

    cond = ' '
    while cond not in 'SN':
        cond = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if cond == 'N':
        break
    elif cond == 'S':
        print('Insira novos dados')
print(f'Existem {maior_18} usuário maiores de 18 anos, {homens} homens cadastrados e {mulheres_menor20} mulheres menores de 20 anos')
