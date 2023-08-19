from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento do possivel recruta: '))
ano_atual = date.today().year
validacao = ano_atual-ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {validacao} anos em {ano_atual}.')
if validacao<18:
    print(f'O individuo ainda irá se alistar daqui a {18-validacao} ano(s)')
    print(f'Seu alistamento será no ano de {(18-validacao)+ano_atual}')
elif validacao==18:
    print('Está na hora de se alistar')
else:
    print(f'O seu alistamento foi no ano de {ano_atual-(validacao-18)}')
    print(f'Passaram-se {validacao-18} anos(s) sem se alistar, apresente-se de imediato!')
