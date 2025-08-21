#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2

largura = float(input("Em metros, digite a largura da parede: "))
altura = float(input("Em metros, digite a altura da parede: "))

area = largura * altura
tinta = 2

print("A quantidade de tinta necessária para pintar a parede é de {} litros".format(area/tinta))
