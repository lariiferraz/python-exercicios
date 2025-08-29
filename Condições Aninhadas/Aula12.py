nome = str(input("Digite seu nome: "))

if nome == "Larissa":
  print("Que nome maravilhoso!")

elif nome == "João" or nome == "Gabriel":
  print("Que nome comum!")

elif nome in "Paula Ana Helena Maria":
  print("Você é uma mulher!")

else: #opcional
  print("Que nome normal!")

print("Tenha um bom dia, {} !".format(nome))