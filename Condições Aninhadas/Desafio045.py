# Crie um programa que faça o computador jogar pedra, papel ou tesoura com você

import time
import random

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)  # espera 1 segundo
print("Pedra, Papel ou Tesoura?")

user = str(input("\nUser: "))
escolha = random.choice(["pedra","papel","tesoura"])
print("\nComputador: {}".format(escolha))

if user == "pedra" and escolha == "pedra":
    print("\nEMPATE! VAMOS NOVAMENTE!")
elif user == "pedra" and escolha == "papel":
    print("\nPONTO PARA O COMPUTADOR!")
elif user == "pedra" and escolha == "tesoura":
    print("\nPONTO PARA O HUMANO!")
elif user == "papel" and escolha == "pedra":
    print("\nPONTO PARA O HUMANO!")
elif user == "papel" and escolha == "papel":
    print("\nEMPATE! VAMOS NOVAMENTE!")
elif user == "papel" and escolha == "tesoura":
    print("\nPONTO PARA O COMPUTADOR!")
elif user == "tesoura" and escolha == "tesoura":
    print("\nEMPATE!!!! VAMOS NOVAMENTE")
elif user == "tesoura" and escolha == "pedra":
    print("\nPONTO PARA O COMPUTADOR!!! ")
elif user == "tesoura" and escolha == "papel":
    print("\nPONTO PARA O HUMANO!!!!!!")