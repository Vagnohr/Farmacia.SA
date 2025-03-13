from tkinter import *
from tkinter import ttk
from DataBase import Database  # Certifique-se de que este módulo está correto
from tkinter import messagebox  # Importa o módulo de caixas de mensagem do tkinter

# Tela de login
jan = Tk()
jan.title("Login de Usuários")
jan.geometry("600x300")
jan.configure(background="purple")
jan.resizable(width=False, height=False)

Titulo = Label(text="Login:", font=("Century Gothic", 25), bg="red", fg="White")
Titulo.place(x=1, y=50)

# Adicionar campos de usuário e senha
usuarioLabel = Label(text="Usuário: ", font=("Century Gothic", 10), bg="ORANGE", fg="White")
usuarioLabel.place(x=1, y=125)
usuarioEntry = ttk.Entry(width=30)
usuarioEntry.place(x=60, y=125)

senhaLabel = Label(text="Senha: ", font=("Century Gothic", 10), bg="ORANGE", fg="White")
senhaLabel.place(x=1, y=155)
senhaEntry = ttk.Entry(width=30, show="*")  # Corrigido para ocultar a senha com "*"
senhaEntry.place(x=55, y=155)

# Função de login
def Login():
    usuario = usuarioEntry.get()
    senha = senhaEntry.get()

    # Conectar ao banco de dados
    try:
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        # Consulta para verificar as credenciais
        cursor.execute("""SELECT * FROM usuario WHERE usuario = %s AND senha = %s""", (usuario, senha))
        VerifiyLogin = cursor.fetchone()

        # Verificar se o usuário foi encontrado
        if VerifiyLogin:
            messagebox.showinfo(title="Info Login", message="Acesso Confirmado. Bem-vindo!")
        else:
            messagebox.showinfo(title="Info Login", message="Acesso Negado. Verifique se o cadastro está no sistema.")

    except Exception as e:
        # Exibir mensagem de erro
        messagebox.showerror(title="Erro de Conexão", message=f"Ocorreu um erro: {e}")

    finally:
        # Garantir que a conexão seja fechada
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Criando botões
LoginButton = ttk.Button(text="Login", width=15, command=Login)
LoginButton.place(x=1, y=180)

# Função para registrar novo usuário
def registrar():
    # Removendo botões de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    # Inserindo widgets de cadastro
    NomeLabel = Label(RIGHT, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(RIGHT, width=30)
    NomeEntry.place(x=120, y=20)

    EmailLabel = Label(RIGHT, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=50)
    EmailEntry = ttk.Entry(RIGHT, width=30)
    EmailEntry.place(x=120, y=70)

    # Função para registrar no banco de dados
    def RegistrarNoBanco():
        nome = NomeEntry.get()
        email = EmailEntry.get()
        usuario = usuarioEntry.get()
        senha = senhaEntry.get()

        # Verifica se todos os campos estão preenchidos
        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro de Registro", message="Preencha todos os campos!")
        else:
            db = Database()
            conn = db.get_connection()
            cursor = conn.cursor()
        # Consulta para verificar as credenciais
            cursor.execute("""SELECT * FROM usuario WHERE usuario = %s AND senha = %s""", (usuario, senha))
            VerifiyLogin = cursor.fetchone()
        # Verificar se o usuário foi encontrado
        if VerifiyLogin:
            messagebox.showinfo(title="Info Login", message="Acesso Confirmado. Bem-vindo!")
        else:
            messagebox.showinfo(title="Info Login", message="Acesso Negado. Verifique se o cadastro está no sistema.")
            # Limpar campos após o registro
        NomeEntry.delete(0, END)
        EmailEntry.delete(0, END)
        usuarioEntry.delete(0, END)
        senhaEntry.delete(0, END)
    Register = ttk.Button(RIGHT, text="Registrar", width=15, command=RegistrarNoBanco)
    Register.place(x=150, y=225)
    # Função para voltar à tela de login
    def VoltarLogin():
        # Remover widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Voltar.place(x=5000)
        # Trazer de volta os widgets de login
        LoginButton.place(x=150)
        RegisterButton.place(x=150)
    Voltar = ttk.Button(RIGHT, text="Voltar", width=15, command=VoltarLogin)
    Voltar.place(x=150, y=255)
RegisterButton = ttk.Button(RIGHT, text="Registrar", width=15, command=registrar)
RegisterButton.place(x=150, y=255)








jan.mainloop()
