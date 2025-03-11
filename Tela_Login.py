#Login de usuarios e de adms
from tkinter import *
from tkinter import ttk 
from Database import Database
from tkinter import messagebox #importa o modulo de caixas de mensagem do tkinter

#tela de login
jan = Tk()
jan.title("Login de Usuarios")
jan.geometry("600x300")
jan.configure(background="purple")
jan.resizable(width=False,height=False)

Titulo = Label(text="Login:",font=("Century Gothic",25),bg="red",fg="White")
Titulo.place(x=1, y=50)

#adicionar campos de usuario e senha
usuarioLabel = Label(text="Usuario: ",font=("Century Gothic",10),bg="ORANGE",fg="White")#cria um albel para o usuario
usuarioLabel.place(x=1, y=125)#posiciona o label no frame direito
usuarioEntry = ttk.Entry(width=30)#cria um campo de entrada para o usuario
usuarioEntry.place(x=60, y=125)#posiciona o campo de entrada

senhaLabel = Label(text="senha: ",font=("Century Gothic",10),bg="ORANGE",fg="White")
senhaLabel.place(x=1, y=155)#posiciona o label no frame direito
senhaEntry = ttk.Entry(width=30, show=".")#cria um campo de entrada para a senha
senhaEntry.place(x=55, y=155)#posiciona o campo de entrada


#função de login
def Login():
        usuario = usuarioEntry.get()  
        senha = senhaEntry.get()
#conectar ao banco de dado
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM usuario WHERE usuario = %s AND senha = %s""",(usuario, senha))
        VerifiyLogin = cursor.fetchone()
    
#ferificar se o usuario foi encontrado
        if VerifiyLogin:
            messagebox.showinfo(title="Info Login", Message ="Acesso Confirmado. Bem Vindo!")
        else:
            messagebox.showinfo(title="Info Login", Message="Acesso Negado, Verifique se o cadastro esta no sistema")

#criando botões
LoginButton = ttk.Button(text="Login",width=15, command=Login)
LoginButton.place(x=1,y=180)

#tela de cadastro


jan.mainloop()