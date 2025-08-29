# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

ano = int(input("Digite seu ano de nascimento: "))
idade = 2025 - ano

if idade <= 9:
  print("Você tem {} anos! Sua categoria é MIRIM".format(idade))
elif idade > 9 and idade <= 14:
  print("Você tem {} anos! Sua categoria é INFANTIL".format(idade))
elif idade > 14 and idade <= 19:
  print("Você tem {} anos! Sua categoria é JUNIOR!".format(idade))
elif idade > 19 and idade <= 25:
  print("Você tem {} anos! Sua categoria é SÊNIOR!".format(idade))
elif idade > 25:
  print("Você tem {} anos! Sua categoria é MASTER!".format(idade))

