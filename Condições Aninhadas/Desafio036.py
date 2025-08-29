# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e quantos anos
# ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorcasa = float(input("Qual o valor da casa: "))
salario = float(input("Qual seu salário? "))
anos = int(input("Em quantos anos você irá pagar: "))

meses = (anos*12)
prestacao = (valorcasa/meses)
limite = salario * 0.30 # poderia calcular a porcentagem por 30/100

if prestacao > limite:
  print("Sua prestação mensal excedeu 30 porcento do seu salário. Seu empréstimo foi negado!")
else:
  print("Seu empréstimo foi aceito! O valor da sua prestação mensal durante {} anos será de {:.2f}!".format(anos,prestacao))

