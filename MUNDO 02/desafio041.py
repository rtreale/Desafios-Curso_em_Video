from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = (ano_atual-ano_nascimento)

print(f'Dada a idade do atleta de {idade} ano(s), ele será alocado para a categoria ', end='')
if idade<=9:
    print('MIRIM!')
elif idade<=14: #nao preciso da condicao entre 9 e 14 pois se pulou a primeira condicao ele verifica a segunda dado elif.
    print('INFANTIL!')
elif idade<=19:
    print('JUNIOR')
elif idade<=20:
    print('SÊNIOR')
else:
    print('MASTER')
