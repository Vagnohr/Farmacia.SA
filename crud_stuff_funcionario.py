import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("farmacia_sa.db")
cursor = conn.cursor()

# Criar a tabela de funcionários, caso ainda não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT,
    cidade TEXT,
    estado TEXT,
    nascimento TEXT,
    contrato TEXT,
    bairro TEXT
)
""")
conn.commit()


# Função para criar/armazenar funcionário no banco
def salvar_funcionario():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    nascimento = entry_nascimento.get()
    contrato = entry_contrato.get()
    bairro = entry_bairro.get()

    if nome and email:
        cursor.execute("""
        INSERT INTO funcionario (nome, email, telefone, cidade, estado, nascimento, contrato, bairro)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, email, telefone, cidade, estado, nascimento, contrato, bairro))
        conn.commit()
        messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
        limpar_campos()
    else:
        messagebox.showwarning("Erro", "Nome e Email são obrigatórios!")


# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_nascimento.delete(0, tk.END)
    entry_contrato.delete(0, tk.END)
    entry_bairro.delete(0, tk.END)


# Função para alternar entre Cadastro e Voltar
def toggle_cadastro():
    if btn_cadastro["text"] == "Cadastro":
        lbl_nascimento.grid(row=6, column=0, sticky="w")
        entry_nascimento.grid(row=6, column=1)
        lbl_contrato.grid(row=7, column=0, sticky="w")
        entry_contrato.grid(row=7, column=1)
        lbl_bairro.grid(row=8, column=0, sticky="w")
        entry_bairro.grid(row=8, column=1)
        btn_cadastro.config(text="Voltar")
    else:
        lbl_nascimento.grid_remove()
        entry_nascimento.grid_remove()
        lbl_contrato.grid_remove()
        entry_contrato.grid_remove()
        lbl_bairro.grid_remove()
        entry_bairro.grid_remove()
        btn_cadastro.config(text="Cadastro")


# Configuração inicial do Tkinter
root = tk.Tk()
root.title("Tela Funcionario - CRUD")

# Campos de entrada
tk.Label(root, text="Nome do Funcionário:").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Telefone:").grid(row=2, column=0, sticky="w")
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1)

tk.Label(root, text="Cidade:").grid(row=3, column=0, sticky="w")
entry_cidade = tk.Entry(root)
entry_cidade.grid(row=3, column=1)

tk.Label(root, text="Estado:").grid(row=4, column=0, sticky="w")
entry_estado = tk.Entry(root)
entry_estado.grid(row=4, column=1)

# Botão de Login (apenas como exemplo)
btn_login = tk.Button(root, text="Login")
btn_login.grid(row=5, column=0, columnspan=2)

# Labels e campos adicionais (inicialmente invisíveis)
lbl_nascimento = tk.Label(root, text="Data de Nascimento:")
entry_nascimento = tk.Entry(root)
lbl_contrato = tk.Label(root, text="Data de Contrato:")
entry_contrato = tk.Entry(root)
lbl_bairro = tk.Label(root, text="Bairro:")
entry_bairro = tk.Entry(root)

# Botão de Cadastro
btn_cadastro = tk.Button(root, text="Cadastro", command=toggle_cadastro)
btn_cadastro.grid(row=9, column=0, columnspan=2)

# Botão para salvar no banco
btn_salvar = tk.Button(root, text="Salvar Funcionário", command=salvar_funcionario)
btn_salvar.grid(row=10, column=0, columnspan=2)

# Inicializar a GUI
root.mainloop()

# Fechar a conexão com o banco de dados ao finalizar
conn.close()
