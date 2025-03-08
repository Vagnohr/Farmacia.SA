#Colocar no Banco de Dados
import mysql.connector
class Database:
    MYSQL_HOST ="localhost",
    MYSQL_USER ="root", 
    MYSQL_PASSWORD ="",
    MYSLQ_DATABASE ="caiobattisti_db" 
    def get_connection():
        return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        Database=MYSLQ_DATABASE
)
    @staticmethod
    def create_user(nome,telefone,email,usuario,senha):
        conn=get_connection()
        cursor=conn.cursor()
        query="insert usuario(nome,telefone,email,usuario,senha)VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(query,(nome,telefone,email,usuario,senha))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod    
    def read_users():
        conn=get_connection()
        cursor=conn.cursor()
        query="SELECT * FROM usuario"
        cursor.execute(query)
        result=cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    
    @staticmethod
    def update_user(nome,telefone,email,usuario,senha,user_id):
        conn=get_connection()
        cursor=conn.cursor()
        query="UPDATE usuario SET nome=%s,telefone=%s,email=%s,usuario=%s,senha=%s WHERE idusuario=%s"
        cursor.execute(query,(nome,telefone,email,usuario,senha,user_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod    
    def delete_user(user_id):
        conn=get_connection()
        cursor=conn.cursor()
        query="DELETE FROM usuario WHERE idusuario=%s"
        cursor.execute(query,(user_id,))
        conn.commit()
        cursor.close()
        conn.close()