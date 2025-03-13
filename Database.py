import mysql.connector

class Database:
    def __init__(self):
        # Configurações do banco de dados
        self.MYSQL_HOST = "localhost"
        self.MYSQL_USER = "root"
        self.MYSQL_PASSWORD = ""
        self.MYSQL_DATABASE = "caiobattisti_db"

    def get_connection(self):
        # Criando uma conexão com o banco de dados
        return mysql.connector.connect(
            host=self.MYSQL_HOST,
            user=self.MYSQL_USER,
            password=self.MYSQL_PASSWORD,
            database=self.MYSQL_DATABASE
        )
db = Database()
# Função para criar um usuário no banco de dados
def login_user(usuario, senha):
    conn = db.get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO usuario (usuario, senha) VALUES (%s, %s)"
    cursor.execute(query, (usuario, senha))
    conn.commit()
    cursor.close()
    conn.close()

