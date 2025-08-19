import mysql.connector

#  Conexão ao banco
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="userroot",
    database=""
)
cursor = con.cursor()

#  Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    idade INT
)
""")

#  Inserir um usuário
sql = "INSERT INTO usuarios (nome, email, idade) VALUES (%s, %s, %s)"
val = ("João Silva", "joao@example.com", 25)
cursor.execute(sql, val)
con.commit()
print(cursor.rowcount, "registro inserido.")

#  Ler usuários
cursor.execute("SELECT * FROM usuarios")
for row in cursor.fetchall():
    print(row)

#  Atualizar usuário
cursor.execute("UPDATE usuarios SET idade = 26 WHERE nome = 'João Silva'")
con.commit()

#  Deletar usuário
cursor.execute("DELETE FROM usuarios WHERE nome = 'João Silva'")
con.commit()

cursor.close()
con.close()
