nome = str(input('Digite o seu nome completo: ')).strip()

pos_1 = nome.find(' ')
pos_2 = nome.rfind(' ')

print('Primeiro nome: {}'.format(nome[:pos_1]))
print('Segundo nome: {}'.format(nome[pos_2+1:]))