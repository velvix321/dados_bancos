import mysql.connector

# Conexão com o MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",         # ou outro usuário, se você criou
    password="password" # substitua pela sua senha do MySQL
)

# Criando um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criando o banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS loja")

print("Banco de dados criado com sucesso!")

# Fechando a conexão
cursor.close()
conexao.close()
