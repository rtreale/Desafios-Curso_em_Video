import math
angulo = float(input('Digite o valor de um ângulo: '))
print('Seno: {:.2f}\n' 'Cosseno: {:.2f}\n' 'Tangente: {:.2f}'.format(math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))
