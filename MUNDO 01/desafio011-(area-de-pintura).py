altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = (altura*largura) #area a ser pintada
galoes = area/2 #galoes de tintas necessarios para pintura

print('Altura: {}\n' 'Largura: {}\n' 'Área: {}m²\n' 'Galões de Tinta: {}L\n'.format(altura, largura, area, galoes))
