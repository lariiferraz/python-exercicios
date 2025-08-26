# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superios a 1.250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

sal = float(input("Qual o valor de seu salário? "))

if sal > 1250:
  newsal = sal*(1+0.10)
  print("Seu salário reajustado com 10 porcento de aumento ficará em: {:.2f}".format(newsal))
else:
  newsal = sal*(1+0.15)
  print("Seu salário reajustado com 15 porcento de aumento ficará em: {:.2f}".format(newsal))