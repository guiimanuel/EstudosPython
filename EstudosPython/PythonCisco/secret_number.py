secret_number = 777
print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")
number= input("Digite o número: ")
number= int(number)
while number != -1:
    if number == secret_number:
        print("Muito bem, trouxa! Você está livre agora.")
        break
    else:
        print("Ha ha! Você está preso no meu loop!")
    number= input('Digite o número novamente ou digite "-1" para parar: ')
    number= int(number)