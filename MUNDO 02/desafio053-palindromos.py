frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
frase_junta = ''.join(palavras)
frase_inversa = frase_junta[::-1] #criando variavel com frase inversa sem o for

'''
#criando variavel com a frase inversa utilizando o for:
for letra in range(len(frase_junta)-1, -1, -1):
    frase_inversa += frase_junta[letra]
'''

print(f'O inverso de {frase_junta} é {frase_inversa}.')
if frase_junta == frase_inversa:
    print('A frase é um palindromo.')
else:
    print('A frase não é um palindromo.')