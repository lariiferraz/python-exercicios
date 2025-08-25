# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
num1 = float(input("Escreva um valor real: "))
arr = math.trunc(num1)
print("A parte inteira do número {} é: {}".format(num1,math.trunc(arr)))