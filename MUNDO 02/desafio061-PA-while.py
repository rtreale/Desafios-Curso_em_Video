a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
c = 0
while c<10:
    print(f'{c+1:2}º termo = {a+r*c}')
    c += 1
