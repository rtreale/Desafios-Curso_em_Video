tabela_brasileirao = ('Sport Recife', 'Goiás', 'Bahia', 'Grêmio', 'Vasco da Gama', 'Fortaleza', 'Bragantino-SP', 'Santos', 'Corinthians', 'Flamengo', 'Atlético-GO', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Coritiba', 'Ceará SC', 'Chapecoense', 'Botafogo', 'Fluminense', 'Internacional')
print('Exibindo os 5 primeiros colocados:')
for c in range(0, 5):
    print(f'{c+1}º colocado: {tabela_brasileirao[c]}')

print('\nExibindo os 4 ultimos colocados:')
for c in range(-4, 0):
    print(f'{c+4+17}º colocado: {tabela_brasileirao[c]}')

print('\nExibindo os times em ordem alfabética:')
print(sorted(tabela_brasileirao))

print(f'\nO time da chapecoense encontra-se na {tabela_brasileirao.index("Chapecoense")+1}º posição.')
