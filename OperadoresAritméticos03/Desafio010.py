# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

saldo = float(input("Quanto há em sua carteira: "))
print("Com este valor, é possível comprar {2} dólares".format(saldo/3.27))

saldo1 = float(input("Quanto há em sua carteira: "))
dolar = float(input("Qual o valor atual do dólar? "))

print("Com estes valores, é possível comprar {} dólares".format(saldo1/dolar))