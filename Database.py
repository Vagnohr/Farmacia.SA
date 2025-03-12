# Importando o módulo do MySQL Connector
import mysql.connector

# Classe para gerenciar o banco de dados
class Database:
    def __init__(self):
        # Configurações do banco de dados
        self.MYSQL_HOST = "localhost"  # Certifique-se de que é uma string
        self.MYSQL_USER = "root"  # Usuário do banco de dados
        self.MYSQL_PASSWORD = ""  # Senha do banco de dados
        self.MYSQL_DATABASE = "caiobattisti_db"  # Nome do banco de dados

    def get_connection(self):
        # Criando uma conexão com o banco de dados
        return mysql.connector.connect(
            host=self.MYSQL_HOST,
            user=self.MYSQL_USER,
            password=self.MYSQL_PASSWORD,
            database=self.MYSQL_DATABASE
        )

# Instância da classe Database
db = Database()

# Função para criar um usuário no banco de dados
def create_user(usuario, senha):
    # Obtém uma conexão com o banco de dados
    conn = db.get_connection()
    cursor = conn.cursor()

    # Query para inserir um novo usuário
    query = "INSERT INTO usuario (usuario, senha) VALUES (%s, %s)"
    cursor.execute(query, (usuario, senha))

    # Confirmando as alterações
    conn.commit()

    # Fechando o cursor e a conexão
    cursor.close()
    conn.close()

# Exemplo de uso
if __name__ == "__main__":
    usuario = "admin"
    senha = "1234"
    create_user(usuario, senha)
    print("Usuário criado com sucesso!")
