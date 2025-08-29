# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# em até 3x no cartão: preço normal
# 3x ou mais: 20% de juros

print(" == MAQUININHA LARISSA == ")
valor = float(input("Insira o valor do produto: "))

opc = int(input(
    "\nQual será sua opção de pagamento?\n\n"
    "[1] À vista no dinheiro ou cheque!\n"
    "[2] À vista no cartão!\n"
    "[3] Em até 3x no cartão, sem juros!\n"
    "[4] 3x ou mais, com 20 porcento de juros\n"
))

if opc == 1:
  desc = valor * 0.10
  desc1 = valor - desc
  print("\n VOCÊ GANHOU 10% DE DESCONTO! O valor total a ser pago é de {:.2f}".format(desc1))
elif opc == 2:
  cartao = valor * 0.05
  cartao1 = valor - cartao
  print("\n VOCÊ GANHOU 5% DE DESCONTO! O valor total a ser pago é de {:.2f}".format(cartao1))
elif opc == 3:
  parc = int(input("\nEm quantas parcelas você gostaria de fazer? 2 ou 3? "))
  if parc == 2:
    valor2 = valor / 2
    print("\nParcelando em 2 vezes, o valor de cada parcela será de {:.2f}\n".format(valor2))
  elif parc == 3:
    valor3 = valor / 3
    print("\nParcelando em 3 vezes, o valor de cada parcela será de {:.2f}\n".format(valor3))
elif opc == 4:
  juros = valor * 0.2
  parc3 = int(input("\nEm quantas vezes você gostaria de fazer? "))
  qnts = (juros + valor)/parc3
  print("\nParcelando em {} vezes, o valor de cada parcela será {}, já adicionado 20 porcento de juros!".format(parc3,qnts))