frase = str(input('Digite uma frase: ')).strip()

print('A letra a, aparecem {} vezes'.format(frase.lower().count('a')))
print('Primeira posição: {}'.format(frase.lower().find('a') + 1))
print('Ultima posição: {}'.format(frase.lower().rfind('a') + 1))
