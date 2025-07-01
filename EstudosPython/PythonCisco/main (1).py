my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escreva seu código aqui.
#
numeros_unicos= []
for numero in my_list:
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)
print("A lista com os elementos exclusivos aqui")
print(numeros_unicos)

