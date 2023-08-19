import math
num = float(input('Digite um número: '))
print('O número: {} tem a parte inteira {}'.format(num, math.trunc(num)))

#from math import trunc - assim eu trago apenas a funcao trunc para o programa sem o modulo completo math
#.format(trunc(num)) - o que muda é que nao colocamos a menção ao modulo math antes de utilizar a função

