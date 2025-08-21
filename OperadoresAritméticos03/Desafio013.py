# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input("Digite o valor de seu salário: "))

aumento = int(salario*(1 + 0.15))

print("O valor de seu novo salário é: {}".format(aumento))