from datetime import datetime
ano_atual = datetime.now().year
dados = {}
dados['nome'] = str(input('Nome: ')).strip()
dados['idade'] = ano_atual - int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] == 0:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = ano_atual - dados['contratação']
    if dados['aposentadoria'] >= 35:
        dados['aposentadoria'] = 'aposentado'
    else:
        dados['aposentadoria'] = dados['idade'] + (35-dados['aposentadoria'])
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')