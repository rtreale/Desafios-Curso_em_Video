print('Preciso de 4 valores inteiros para começar a minha analise.')
n = (int(input('1º Valor: ')), int(input('2º Valor: ')), int(input('3º Valor: ')), int(input('4º Valor: ')))
print(f'Valores digitados {n}')
#a)
print(f'a) O numero 9 apareceu {n.count(9)} vezes.')

#b)
if 3 in n:
    print(f'b) O número 3 foi digitado na {n.index(3)+1}º posição')
else:
    print('b) O número 3 não foi digitado.')

#b) como eu havia feito. mais trabalhoso do que usar o metodo in no if.
'''pos = -1
for c in range(0, 4):
    if n[c] == 3:
        pos = c+1
        break
if pos==-1:
    print('b) O numero 3 não foi digitado.')
elif pos!=-1:
    print(f'b) O numero 3 foi digitado na {pos}º posição')
'''

#c)
cont = 0
for c in n:
    if c%2==0:
        cont += 1
if cont == 0:
    print('c) Não houve ocorrencia de numeros pares.')
elif cont != 0 :
    print('c) Os numeros pares foram: ', end='')
    for c in n:
        if c%2==0:
            print(c, end=' ')
