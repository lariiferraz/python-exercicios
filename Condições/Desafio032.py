# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input("Digite um ano (xxxx): "))
bis = ano%4

if bis == 0:
  print("O ano é bissexto!")
else:
  print("O ano não é bissexto!")