#Login de usuarios e de adms
from tkinter import *
from tkinter import ttk 
from Database import Database
from tkinter import messagebox #importa o modulo de caixas de mensagem do tkinter
from tkinter import self
#cria a janela
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
        cursor.execute("""SELECT * FROM usuario1 WHERE usuario = %s AND senha = %s""",(usuario, senha))
        VerifiyLogin = cursor.fetchone()
    
#ferificar se o usuario foi encontrado
        if VerifiyLogin:
            messagebox.showinfo(title="Info Login", Message ="Acesso Confirmado. Bem Vindo!")
        else:
            messagebox.showinfo(title="Info Login", Message="Acesso Negado, Verifique se o cadastro esta no sistema")

#criando botões
LoginButton = ttk.Button(text="Login",width=15, command=Login)
LoginButton.place(x=1,y=180)

'''#criação de WIDGETS
self.create_widgets()
        
def create_widgets(self):
        #Labels
        ttk.Label(self.root,text="Nome: ").grid(row=0,column=0)
        ttk.Label(self.root,text="telefone: ").grid(row=1,column=0)
        ttk.Label(self.root,text="Email: ").grid(row=2,column=0)
        ttk.Label(self.root,text="Usuario: ").grid(row=3,column=0)
        ttk.Label(self.root,text="senha: ").grid(row=4,column=0)
        ttk.Label(self.root,text="User ID(for update/delete): ").grid(row=5,column=0)

        #criar as caixas para digitar os valores
        self.nome_entry = tk.Entry(self.root)
        self.telefone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.usuario_entry = tk.Entry(self.root)
        self.senha_entry = tk.Entry(self.root)
        self.user_ID_entry = tk.Entry(self.root)
        
        self.nome_entry.grid(row=0,column=1)
        self.telefone_entry.grid(row=1,column=1)
        self.email_entry.grid(row=2,column=1)
        self.usuario_entry.grid(row=3,column=1)
        self.senha_entry.grid(row=4,column=1)
        self.user_ID_entry.grid(row=5,column=1)
        #botoes crud
        ttk.Button(self.root,text="criar Usuario",command=self.create_user).grid(row=6,column=0,columnspan=1)
        
        
        def create_user(self):
            nome = self.nome_entry.get()
            telefone = self.telefone_entry.get()
            email = self.email_entry.get()
            usuario = self.usuario_entry.get()
            senha = self.senha_entry.get()

        if nome and telefone and email and usuario and senha:
            create_user(nome,telefone,email,usuario,senha)
            self.nome_entry.delete =(0,tk.END)
            self.telefone_entry.delete =(0,tk.END)
            self.email_entry.delete =(0,tk.END)
            self.usuario_entry.delete =(0,tk.END)
            self.senha_entry.delete =(0,tk.END)
            messagebox.showinfo("Successo","Usuario criado com Sucesso")
        else:
           messagebox.showerror("Error","Todos os campos são obrigatorios!")
'''

jan.mainloop()