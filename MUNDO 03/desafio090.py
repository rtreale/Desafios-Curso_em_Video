boletim = {}
boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
elif boletim['Média'] <5:
    boletim['Situação'] = 'Reprovado'
else:
    boletim['Situação'] = 'Recuperação'
for k, v in boletim.items():
    print(f'{k} é igual a {v}')
