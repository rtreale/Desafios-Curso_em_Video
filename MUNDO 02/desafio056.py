idade_media = 0
homem_velho = ''
mulheres_novas = 0
cont = 0

for c in range(1, 5):
    print(f'Entre com os seguintes dados para a {c}º pessoa:')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M] = masculino / [F] = feminino: ')).strip().upper()
    idade_media += idade

    if c == 1 and sexo == 'M':
    #if c == 1 and sexo in 'Mm': #a condicao in abrange F maisculo e f minusculo, podendo desprezar o uso do upper na string
        cont = idade
        homem_velho = nome
    if sexo == 'M' and idade>cont:
    #if sexo in 'Mm' and idade>cont: #a condicao in abrange F maisculo e f minusculo, podendo desprezar o uso do upper na string
        cont = idade
        homem_velho = nome
    if sexo == 'F' and idade<20:
    #if sexo in 'Ff' and idade<20: #a condicao in abrange F maisculo e f minusculo, podendo desprezar o uso do upper na string
        mulheres_novas += 1

print(f'''Média de idade do grupo: {idade_media/4} anos
Nome do homem mais velho: {homem_velho}
Mulheres com menos de 20 anos: {mulheres_novas}''')
