nome = str(input('Digite o seu nome completo: ')).strip() #a funcao strip retira os espacos iniciais e finais da string
print('Nome em letras maiusculas: {}'.format(nome.upper()))
print('Nome em letras minusculas: {}'.format(nome.lower()))
print('O nome contém {} letras'.format(len(nome) - nome.count(' ')))

#print('O primeiro nome contém {} letras'.format(nome.find(' ')))

nome_list = nome.split() #split corta as strings com base nos espacos e cria uma lista
print('O primeiro nome {} contem {} letras'.format(nome_list[0], len(nome_list[0])))
