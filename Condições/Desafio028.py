# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador
# O programa deverá escrever na teça se o usuário venceu ou perdeu

import random

numero = random.choice([0,1,2,3,4,5])
valor = int(input("Qual valor eu pensei? "))

if numero != valor:
  print("Errou! Eu pensei em {}".format(numero))
else:
  print("Acertou! Eu também pensei em {}".format(numero))