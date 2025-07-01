#DICIONARIOS EM PYTHON

#chave:valor
#usada com {} ou dict().
#chave sempre será uma string, valor pode ser o tipo que eu quiser.

#EX.1:
#pessoa1= {"nome":"Maria","idade":15,"cidade":"Jaboatão"}
#pessoa2= {"nome":"José","idade":18,"cidade":"Recife"}
#pessoa3={"nome":"João","idade":16}


#EX.2:
#não é preciso colocar aspas na chave quando criar usando um dict().
#pessoa1= dict(nome="José", idade=16, cidade="Recife")

#acessando a chave do dict.
#print(pessoa1["nome"])
#print(pessoa1["cidade"])

#get retorna NONE se o dict não estiver definido.
#podemos colocar uma alternativa, se não estiver definido.
#EX.:
#print(pessoa2.get("cidade"))
#print(pessoa2.get("cidade","cidade nao informada"))

#adicionar ou alterar o elem. do dict.
#pessoa2["nome"]= "José da Silva"
#pessoa2["cidade"]= "Paulista"
#print(pessoa2)

#atualizar multiplos valores
#pessoa1.update({"idade":32, "email":"maria32@gmail.com"})

#remover itens
#.pop retorna o valor que removeu
#pessoa2.pop("idade")

#obter todas as chaves
#pessoa1.keys()

#obter todos os valores
#pessoa1.values()

#obter par chave:valor
#pessoa1.items()

#dicionario dentro de outro dicionario dentro
"""usuarios= {
    "joão": {
        "nome": "João Silva",
        "email":"joao@gmail.com"
    },
    "maria": {
        "nome": "Maria Souza",
        "email": "maria@gmail.com"
    }
}"""

#lista de dicionarios

joão= {"nome": "João Silva","email":"joao@gmail.com"}
maria= {"nome": "Maria Souza","email": "maria@gmail.com"}
usuarios=[joão,maria]
print(usuarios[0]["email"])
print(usuarios[1]["nome"])