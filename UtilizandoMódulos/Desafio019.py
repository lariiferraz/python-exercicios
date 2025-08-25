# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

import random 
nome1 = str(input("Primeiro nome: ")) 
nome2 = str(input("Segundo nome: ")) 
nome3 = str(input("Terceiro nome: ")) 
nome4 = str(input("Quarto nome: "))

lista = [nome1,nome2,nome3,nome4]

escolhido = random.choice(lista) #escolhe um valor

print("O aluno escolhido é: {}".format(escolhido))
