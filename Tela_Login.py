#Login de usuarios e de adms
from tkinter import *
from tkinter import ttk 
from Database import Database

#cria a janela
jan = Tk()
jan.title("Login de Usuarios")
jan.geometry("600x300")
jan.configure(background="purple")
jan.resizable(width=False,height=False)

Titulo = Label(text="Login:",font=("Century Gothic",25),bg="red",fg="White")
Titulo.place(x=1, y=50)

#adicionar campos de usuario e senha
nomeLabel = Label(text="Nome: ",font=("Century Gothic",10),bg="ORANGE",fg="White")#cria um albel para o usuario
nomeLabel.place(x=1, y=100)#posiciona o label no frame direito
nomeEntry = ttk.Entry(width=30)#cria um campo de entrada para o usuario
nomeEntry.place(x=55, y=100)#posiciona o campo de entrada

usuarioLabel = Label(text="Usuario: ",font=("Century Gothic",10),bg="ORANGE",fg="White")#cria um albel para o usuario
usuarioLabel.place(x=1, y=125)#posiciona o label no frame direito
usuarioEntry = ttk.Entry(width=30)#cria um campo de entrada para o usuario
usuarioEntry.place(x=60, y=125)#posiciona o campo de entrada

emailLabel = Label(text="email: ",font=("Century Gothic",10),bg="ORANGE",fg="White")#cria um albel para o usuario
emailLabel.place(x=1, y=150)#posiciona o label no frame direito
emailEntry = ttk.Entry(width=30)#cria um campo de entrada para o usuario
emailEntry.place(x=50, y=150)#posiciona o campo de entrada

senhaLabel = Label(text="senha: ",font=("Century Gothic",10),bg="ORANGE",fg="White")
senhaLabel.place(x=1, y=175)#posiciona o label no frame direito
senhaEntry = ttk.Entry(width=30, show=".")#cria um campo de entrada para a senha
senhaEntry.place(x=55, y=175)#posiciona o campo de entrada

#criando botões
LoginButton1 = ttk.Button(text="Login")
LoginButton1.place(x=1,y=200)

#função de login
def Login():
    nome = nomeEntry.get()
    usuario = usuarioEntry.get()
    email = emailEntry.get()   
    senha = senhaEntry.get()

#conectar ao banco de dado
    db = Database()
    db.cursor.execute("""SELECT * FROM usuario2 WHERE usuario = %s""",(usuario, senha))

jan.mainloop()