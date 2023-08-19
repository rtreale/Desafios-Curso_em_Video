boletim = [[], [], []]
#    nome (0)/ notas (1) / media (2)
while True:
    boletim[0].append(str(input('Nome: ')))
    boletim[1].append(float(input('Nota 1: ')))
    boletim[1].append(float(input('Nota 2: ')))
    request = ' '
    while request not in 'SN':
        request = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if request == 'N':
        break

for c in range(0, len(boletim[1]), 2):
    media = (boletim[1][c] + boletim[1][c + 1]) / 2
    boletim[2].append(media)

print(boletim)

print('-'*28)
print(f'{"No.":<5} {"NOME":15} {"MÉDIA":4}')
print('-'*28)
for c in range(0, len(boletim[0])):
    print(f'{c:<5} {boletim[0][c]:15} {boletim[2][c]:4.1f}')
print('-'*28)

while True:
    no = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if no == 999:
        break
    else:
        print(f'As notas de {boletim[0][no]} são: [{boletim[1][(no*2)]}, {boletim[1][(no*2)+1]}]')
