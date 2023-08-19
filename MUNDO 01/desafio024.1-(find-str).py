cidade = str(input('Qual cidade você nasceu? ')).strip().upper()
lista = cidade.split()
verificador = 'SANTO' in lista[0]

print(verificador)