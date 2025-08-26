# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando 0,50 por Km para viagens 
# de até 200km e 0,45 para viagens mais longas

dist = float(input("Qual a distância da sua viagem em KM?: "))

if dist <= 200:
  valor = dist*0.50
  print("O valor da suas viagem será: {}".format(valor))
else:
  valor = dist*0.45
  print("O valor da sua viagem será: {}".format(valor))