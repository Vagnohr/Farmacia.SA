#Login de usuarios e de adms
from tkinter import *
from tkinter import ttk 

#cria a janela
jan = Tk()
jan.title("Login de Usuarios")
jan.geometry("600x300")
jan.configure(background="purple")
jan.resizable(width=False,height=False)

#adicionar campos de usuario e senha
usuarioLabel = Label(text="Usuario: ",font=("Century Gothic",10),bg="ORANGE",fg="White")#cria um albel para o usuario
usuarioLabel.place(x=5, y=100)#posiciona o label no frame direito
usuarioEntry = ttk.Entry(width=30)#cria um campo de entrada para o usuario
usuarioEntry.place(x=65, y=100)#posiciona o campo de entrada

senhaLabel = Label(text="Senha: ",font=("Century Gothic",10),bg="ORANGE",fg="White")#cria um albel para a senha
senhaLabel.place(x=5, y=125)#posiciona o label no frame direito
senhaEntry = ttk.Entry(width=30, show=".")#cria um campo de entrada para a senha
senhaEntry.place(x=60, y=125)#posiciona o campo de entrada

#criando botões
LoginButton = ttk.Button(text="Login")
LoginButton.place(x=5,y=150)
jan.mainloop()