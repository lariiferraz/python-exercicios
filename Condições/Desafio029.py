# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar 7,00 para cada KM acima do limite

vel = float(input("Digite sua velocidade: "))

if vel > 80:
  valor = (vel-80)*7
  print("Você foi multado, sua multa custa: {:.2f}".format(valor))
else:
  print("Você não foi multado")