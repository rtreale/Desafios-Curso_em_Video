n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

if media<5.0:
    print(f'Aluno reprovado com média: {media:.1f}')
elif media>=7.0:
    print(f'Aluno aprovado com média: {media:.1f}')
else:
    print(f'Aluno em recuperação devido a media: {media:.1f}')