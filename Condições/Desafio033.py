# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

lista = [num1,num2,num3]
lista.sort()

print(f"O menor número é o {lista[0]} e o maior é o {lista[2]}")