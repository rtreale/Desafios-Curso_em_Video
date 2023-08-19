peso = float(input('Qual peso do paciente em [kg]? '))
altura = float(input('Qual a altura do paciente em [m]? '))
imc = peso/(altura**2)

print(f'Com base no peso de {peso}[kg] e altura de {altura}[m], o paciente apresenta IMC = {imc:.1f}')
print('Desta forma o paciente encontra-se: ', end='')
if imc<18.5:
    print('ABAIXO DO PESO!')
elif imc<25:
    print('COM O PESO IDEAL!')
elif imc<30:
    print('COM SOBREPESO!')
elif imc<40:
    print('COM OBESIDADE!')
else:
    print('COM OBESIDADE MÓRBIDA!')
