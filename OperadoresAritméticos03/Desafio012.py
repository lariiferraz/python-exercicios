# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

valor = float(input("Qual o valor do produto?: "))
desconto = valor * (1 - 0.05)

print("O valor do produto com um desconto de 5% é de {}".format(desconto))