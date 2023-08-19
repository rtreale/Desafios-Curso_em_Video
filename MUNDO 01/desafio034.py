salario = float(input('Digite o salario do funcionario: '))

if (salario > 1250):
    print('Novo salario: R${:.2f}'.format(salario*1.10))
else:
    print('Novo salario: R${:.2f}'.format(salario*1.15))
