year = int(input("Digite um ano: "))
if year < 1582:
  print("Não dentro do período do calendário gregoriano")
else:
    if year%4 != 0:
        print("É um ano comum")
    elif year%100 != 0:
        print("É um ano bissexto")
    elif year%400 != 0:
        print("É um ano comum")
    else:
        print("É um ano bissexto")
  # Escreve o bloco se-então aqui
 