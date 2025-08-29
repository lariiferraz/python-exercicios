# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num1 = int(input("Digite um número: "))

print("Qual será a base de conversão: "
"[1] Converter para BINÁRIO " 
"[2] Converter para OCTAL " 
"[3] Converter para HEXA ")

escolha = int(input("Sua opção: "))

if escolha == 1:
  binario = (bin(num1)[2:])
  print("O número {} em BINÁRIO é {}".format(num1,binario))
elif escolha == 2:
  octal = (oct(num1)[2:])
  print("O número {} em OCTAL é {}".format(num1,octal))
elif escolha == 3:
  hexa = (hex(num1)[2:])
  print("O número {} em HEXA é {}".format(num1,hexa))