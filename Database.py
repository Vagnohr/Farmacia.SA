#Colocar no Banco de Dados
import mysql.connector

class Database:
    def __init__(self):
        #conecta ao banco de dados
        self.conn = mysql.connector.connect(
            host ="localhost",
            user ="root", 
            password ="",
            Database ="CaioBattisti_db" 
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS 
        usuario1(                    
            idusuario INT AUTO_INCREMENT PRIMARY KEY               
            nome TEXT (255),               
            email TEXT (255),               
            usuario TEXT (255),  
            senha TEXT (255)                           
        );''')
        self.conn.commit()

    print("Conectando ao Banco de Dados")