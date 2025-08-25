# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa

import math
opo = float(input("Digite o valor do cateto oposto: "))
adj = float(input("Digite o valor do cateto adjacente: "))

#hip = math.sqrt(opo**2 + adj**2)
hip = math.hypot(opo,adj)

print("O valor da hipotenusa é {}".format(hip))