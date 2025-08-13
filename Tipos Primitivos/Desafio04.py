#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ela

algo = (input("Escreva algo: "))

print(type(algo))
print(algo.isalnum())
print(algo.isdecimal())
print(algo.isupper())
print(algo.islower())
print(algo.isascii())
