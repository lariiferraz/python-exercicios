# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5 Abaixo do peso
# Entre 18.5 e 25: Peso ideial
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: obesidade mórbida

peso = float(input("Qual seu peso? "))
alt = float(input("Qual sua altura? "))

imc = peso/alt**2
#print("Seu IMC deu {:.2f}".format(imc))

if imc < 18.5:
  print("Seu IMC deu {:.2f}, você está ABAIXO DO PESO.".format(imc))
elif imc > 18.5 and imc <= 25:
  print("Seu IMC deu {:.2f}, vocÊ está no PESO IDEAL.".format(imc))
elif imc > 25 and imc <= 30:
  print("Seu IMC deu {:.2f}, você está com SOBREPESO".format(imc))
elif imc > 30 and imc <= 40:
  print("Seu IMC deu {:.2f}, você está com OBESIDADE".format(imc))
else: 
  print("Seu IMC deu {:.2f}, você está com OBESIDADE MÓRBIDA".format(imc))
