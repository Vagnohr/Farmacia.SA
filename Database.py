#Colocar no Banco de Dados
import mysql.connector
class Database:
    def __init__(self):
        self.MYSQL_HOST ="localhost",
        self.MYSQL_USER ="root", 
        self.MYSQL_PASSWORD ="",
        self.MYSLQ_DATABASE ="caiobattisti_db" 

    def get_connection(self):
        return mysql.connector.connect(
            host=self.MYSQL_HOST,
            user=self.MYSQL_USER,
            password=self.MYSQL_PASSWORD,
            Database=self.MYSLQ_DATABASE
)
db = Database()

def get_connection():
    return db.get_connection()
def create_user(usuario,senha):
    conn=get_connection()
    cursor=conn.cursor()
    query="insert usuario(usuario,senha)VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(query,(usuario,senha))
    conn.commit()
    cursor.close()
    conn.close()