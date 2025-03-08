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
def create_user(nome,telefone,email,usuario,senha):
    conn=get_connection()
    cursor=conn.cursor()
    query="insert usuario(nome,telefone,email,usuario,senha)VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(query,(nome,telefone,email,usuario,senha))
    conn.commit()
    cursor.close()
    conn.close()

       
def read_users():
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT * FROM usuario"
    cursor.execute(query)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result
    
    
def update_user(nome,telefone,email,usuario,senha,user_id):
    conn=get_connection()
    cursor=conn.cursor()
    query="UPDATE usuario SET nome=%s,telefone=%s,email=%s,usuario=%s,senha=%s WHERE idusuario=%s"
    cursor.execute(query,(nome,telefone,email,usuario,senha,user_id))
    conn.commit()
    cursor.close()
    conn.close()

    
def delete_user(user_id):
    conn=get_connection()
    cursor=conn.cursor()
    query="DELETE FROM usuario WHERE idusuario=%s"
    cursor.execute(query,(user_id,))
    conn.commit()
    cursor.close()
    conn.close()