# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# o segundo valor é maior
# não existe valor maior, os dois são iguais

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
  print("O primeiro valor, {}, é maior que o segundo, {}".format(num1,num2))
elif num2 > num1:
  print("O segundo valor, {}, é maior que o primeiro, {}".format(num2,num1))
elif num1 == num2:
  print("Os valores são iguais! Ambos são {}".format(num1))