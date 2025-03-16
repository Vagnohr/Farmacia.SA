from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# Classe de conexão com o banco de dados
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("farmacia.db")
        self.cursor = self.conn.cursor()

    def get_connection(self):
        return self.conn


# Função de autenticação para login
def autenticar_usuario(email, telefone):
    try:
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        # Consulta para verificar as credenciais no banco de dados
        cursor.execute("SELECT * FROM funcionario WHERE email = ? AND telefone = ?", (email, telefone))
        usuario = cursor.fetchone()
        
        if usuario:
            return True  # Usuário encontrado
        else:
            return False  # Usuário não encontrado

    except Exception as e:
        messagebox.showerror("Erro de Conexão", f"Ocorreu um erro ao conectar ao banco de dados: {e}")
        return False

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


# Tela principal
jan = Tk()
jan.title("Login de Funcionários")
jan.geometry("600x300")
jan.configure(background="purple")
jan.resizable(width=False, height=False)

Titulo = Label(jan, text="Login de Funcionários", font=("Century Gothic", 25), bg="red", fg="White")
Titulo.place(x=1, y=50)

# Adicionar campos de login (email e telefone)
emailLabel = Label(jan, text="Email: ", font=("Century Gothic", 10), bg="ORANGE", fg="White")
emailLabel.place(x=1, y=125)
emailEntry = ttk.Entry(jan, width=30)
emailEntry.place(x=60, y=125)

telefoneLabel = Label(jan, text="Telefone: ", font=("Century Gothic", 10), bg="ORANGE", fg="White")
telefoneLabel.place(x=1, y=155)
telefoneEntry = ttk.Entry(jan, width=30)
telefoneEntry.place(x=75, y=155)

# Função de login
def Login():
    email = emailEntry.get()
    telefone = telefoneEntry.get()

    if autenticar_usuario(email, telefone):
        messagebox.showinfo(title="Login", message="Login realizado com sucesso!")
    else:
        messagebox.showwarning(title="Erro", message="Email ou telefone incorretos. Tente novamente.")

# Botões principais
LoginButton = ttk.Button(jan, text="Login", width=15, command=Login)
LoginButton.place(x=150, y=200)

jan.mainloop()
