# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

import math
num = int(input("Digite um valor: "))

valor = num%2

if valor == 0:
  print("Seu número é par!")
else:
  print("Seu número é ímpar!")
