#Tela de login para ADM e USUARIOS:
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from dataclasses import Database

#aicionar campos de usuario e senha
usuarioLabel = Label(RIGHT, text="Usuario: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
usuarioLabel.place(x=5, y=100)
usuarioEntry = ttk.Entry(RIGHT, width=30)
usuarioEntry.place(x=120, y=115)

senhaLabel = Label(RIGHT, text="Senha: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
senhaLabel.place(x=5, y=150)
senhaEntry = ttk.Entry(RIGHT, width=30, show=".")
senhaEntry.place(x=120, y=165)

def Login():
    usuario = usuarioEntry.get()
    senha = senhaEntry.get()

    db = Database()
    db.cursor.execute("""SELECT * FROM usuario1 WHERE usuario = %s""",(usuario, senha))
    VerifiyLogin = db.cursor.fetchone()

    if VerifiyLogin:
        messagebox.showinfo(title="Info Login", Message ="Acesso Confirmado. Bem Vindo!")
    else:
        messagebox.showinfo(title="Info Login", Message="Acesso Negado, Verifique se o cadastro esta no sistema")

LoginButton = ttk.Button(RIGHT, text="Login",width=15, command=Login)
LoginButton.place(x=150,y=225)