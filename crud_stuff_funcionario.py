import sqlite3

def create_table():
    conn = sqlite3.connect("funcionario.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT,
        cidade TEXT,
        estado TEXT,
        bairro TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_funcionario(nome, email, telefone, cidade, estado, bairro):
    conn = sqlite3.connect("funcionario.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO funcionario (nome, email, telefone, cidade, estado, bairro)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, email, telefone, cidade, estado, bairro))
    conn.commit()
    conn.close()

def read_funcionarios():
    conn = sqlite3.connect("funcionario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionario")
    funcionarios = cursor.fetchall()
    conn.close()
    return funcionarios

# Criar a tabela ao carregar o módulo
create_table()
