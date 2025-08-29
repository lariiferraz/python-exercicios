# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 a 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1+nota2)/2

if media < 5: 
  print("REPROVADO! Sua média ficou {}! Vai estudar!".format(media))
elif media >= 5 and media < 7:
  print("Você está de recuperação! Sua média ficou {:.1f}! Vai estudar!".format(media))
elif media >= 7:
  print("APROVADO, PORRA!!!!!!!! Sua média ficou em {}".format(media))