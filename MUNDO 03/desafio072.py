num_extenso = ('zero', 'um', 'dois', 'três', 'quatro',
               'cinco', 'seis', 'sete', 'oito', 'nove',
               'dez', 'onze', 'doze', 'treze', 'quatorze',
               'quinze', 'dezesseis', 'dezessete', 'dezoito',
               'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0<=num<=20:
        break
    else:
        print('Valor inválido, tente novamente.')
print(f'Você digitou o número {num_extenso[num]}')