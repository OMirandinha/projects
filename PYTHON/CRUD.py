#A simple CRUD I made in Python with a little help from Youtube tutorials :)

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password=' ',
    database='crud_python',
)

cursor = conexao.cursor()

# CREATE
nome_produto = "Daedric Sword"
valor = 250
command = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(command)
conexao.commit() # used to edit the database




# READ
command = f'SELECT * FROM vendas'
cursor.execute(command)
result = cursor.fetchall() # reads the database
print(result)

# UPDATE

nome_produto = "Daedric Sword"
valor = 300
command = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(command)

# Delete

command = f'DELETE FROM vendas WHERE idvendas = 1'
cursor.execute(command)
conexao.commit()

cursor.close()
conexao.close()
