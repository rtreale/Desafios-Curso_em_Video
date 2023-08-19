import random

aluno_1 = str(input('Nome do aluno 1: '))
aluno_2 = str(input('Nome do aluno 2: '))
aluno_3 = str(input('Nome do aluno 3: '))
aluno_4 = str(input('Nome do aluno 4: '))

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

print('O aluno sorteado foi: {}'.format(random.choice(lista)))
