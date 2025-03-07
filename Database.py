#Colocar no Banco de Dados
import mysql.connector

class Database:
    def __init__(self):
        #conecta ao banco de dados
        self.conn = mysql.connector.connect(
            host ="localhost",
            user ="root", 
            password ="",
            Database ="farmacia_sa" 
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS 
        usuario1(                    
            idusuario INT AUTO_INCREMENT PRIMARY KEY                                          
            usuario TEXT (255),  
            senha TEXT (255)                           
        );''')
        self.conn.commit()

    print("Conectando ao Banco de Dados")
    
#Método para buscar os Dados de um usuario no Banco de Dados
    def buscar(self,idusuario):
        self.cursor.execute("SELECT * FROM usuario1 WHERE idusuario=%s",(idusuario))
        self.conn.commit()