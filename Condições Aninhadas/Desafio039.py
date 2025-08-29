# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ela ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

ano = int(input("Digite seu ano de nascimento: "))

idade = 2025 - ano
qnd = 18 - idade

if idade > 18:
  print("Já passou da épóca de se alistar!")
elif idade < 18:
  print("Você ainda precisará se alistar! Falta {} anos para chegar sua vez!".format(qnd))
elif idade == 18:
  print("Está na hora de se alistar!")
