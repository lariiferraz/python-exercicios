# sabe o limite
for c in range (1,2):
  print(c)
print("FIM")

# sabendo ou não o limite
c = 1 
while c < 2:
  print(c)
  c = c + 1 
  # ou c += 1
print("FIM")

#for c in range (1,5):
#  n = int(input("Digite um valor: "))
# print("FIM")

# criando laços indeterminadamente
# r = "S"
# n = 1
# while r == "S":
#  n = int(input("Digite um valor: "))
#  r = str(input("Quer continuar? [S/N] ")).upper()
# print("FIM")

n = 1
par = impar = 0 # as duas variáveis começam com zero
while n != 0:
  n = int(input("Digite um valor: "))
  if n % 2 == 0: # verifica se o número é par
    par += 1 # atalho para par = par + 1, é necessário pois estamos contando quantas vezes aconteceu
  else:
    impar += 1
print("Você digitou {} números pares e {} números ímpares!".format(par,impar))

# se for par, ele aumenta o contador par em +1
# se for impar, ele aumenta o contador impar em +1

# Acabei de encontrar mais um número par -> soma 1 no total de pares 
# Acabei de encontrar mais um número impar -> soma 1 no total de impares