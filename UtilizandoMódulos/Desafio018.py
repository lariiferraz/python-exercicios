# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
ang1 = float(input("Digite o valor do ângulo: "))

# converter em radianos
rad = math.radians(ang1)

sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print("O valor do seno é {:.6f}, do cosseno {:.6f} e da tangente {:.6f}".format(sen,cos,tan))