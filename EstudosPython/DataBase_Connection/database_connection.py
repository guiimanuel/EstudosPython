import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1", # servidor MySQL
    user="root", # usuario
    passwd="Guilherme0708_", # senha
    database="proj_livraria" # nome do banco (Schema)
)

cursor = conexao.cursor() # execucao de comandos (insert,update,query,delete, etc...)


cursor.close() # fecha cursor
conexao.close() # fecha conexao

print(conexao)