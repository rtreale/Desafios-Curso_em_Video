import math
co = float(input('Digite o valor do cateto oposto: '))     #co-cateto oposto
ca = float(input('Digite o valor do cateto adjacente: '))    #ca-cateto adjacente
hypot = math.hypot(co, ca)

print('Cateto oposto: {}\n' 'Cateto adjacente: {}\n' 'Hipotenusa: {:.2f}'.format(co, ca, hypot))
