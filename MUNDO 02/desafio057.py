sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #o colchete no fim é pra pegar somente a primeira letra
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))