import sqlite3

#Conexao com o banco de dados
con = sqlite3.connect('projeto_1.db')
cur = con.cursor()

#Criacao das tabelas
cur.execute('''CREATE TABLE IF NOT EXISTS clientes
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL)''')

#confirmar e fechar
con.commit()
con.close()