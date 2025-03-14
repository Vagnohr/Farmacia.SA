import tkinter as tk
from tkinter import messagebox
from crud_stuff_fornecedores import add_supplier,read_suppliers
class CRUDApp:
    def __init__(self,root):
        self.root=root
        self.root.title("FORNECEDORES")
        #criação de widgets
        self.create_widgets()
    def create_widgets(self):
        #Labels
        tk.Label(self.root,text="Nome:").grid(row=0,column=0)
        tk.Label(self.root,text="email:").grid(row=1,column=0)
        tk.Label(self.root,text="Produto Fornecido:").grid(row=2,column=0)
        tk.Label(self.root,text="Quantia Mensal:").grid(row=3,column=0)
        tk.Label(self.root,text="Tipo de Transporte:").grid(row=4,column=0)
        tk.Label(self.root,text="Cidade:").grid(row=5,column=0)
        tk.Label(self.root,text="Estado:").grid(row=6,column=0)
        tk.Label(self.root,text="Id Fornecedor (for update/delete):").grid(row=7,column=0)
        #criar as caixas para digitar os valores
        self.nome_entry=tk.Entry(self.root)
        self.email_entry=tk.Entry(self.root)
        self.produto_fornecido_entry=tk.Entry(self.root)
        self.quantia_mensal_entry=tk.Entry(self.root)
        self.tipo_transporte_entry=tk.Entry(self.root)
        self.cidade_entry=tk.Entry(self.root)
        self.estado_entry=tk.Entry(self.root)
        self.idfornecedor_entry=tk.Entry(self.root)
        self.nome_entry.grid(row=0,column=1)
        self.email_entry.grid(row=1,column=1)
        self.produto_fornecido_entry.grid(row=2,column=1)
        self.quantia_mensal_entry.grid(row=3,column=1)
        self.tipo_transporte_entry.grid(row=4,column=1)
        self.cidade_entry.grid(row=5,column=1)
        self.estado_entry.grid(row=6,column=1)
        self.idfornecedor_entry.grid(row=7,column=1)
        #botões do crud
        tk.Button(self.root,text="Adicionar fornecedor",command=self.add_supplier).grid(row=8,column=0,columnspan=1)
        tk.Button(self.root,text="Listar fornecedores",command=self.read_suppliers).grid(row=8,column=1,columnspan=1)
        self.text_area=tk.Text(self.root,height=10,width=80)
        self.text_area.grid(row=10,column=0,columnspan=4)
    def add_supplier(self):
        nome=self.nome_entry.get()
        produtofornecido=self.produto_fornecido_entry.get()
        quantiamensal=self.quantia_mensal_entry.get()
        usuario=self.email_entry.get()
        transporte=self.tipo_transporte_entry.get()
        cidade=self.cidade_entry.get()
        estado=self.estado_entry.get()
        if nome and produtofornecido and quantiamensal and usuario and transporte and cidade and estado:
            add_supplier(nome,produtofornecido,quantiamensal,usuario,transporte,cidade,estado)
            self.nome_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.produto_fornecido_entry.delete(0,tk.END)
            self.quantia_mensal_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            messagebox.showinfo("Successo","Fornecedor adicionado com sucesso")
        else:
            messagebox.showerror("Error","Todos os campos são obrigatórios")
    def read_suppliers(self):
        suppliers=read_suppliers()
        self.text_area.delete(1.0,tk.END)
        for supplier in suppliers:
            self.text_area.insert(tk.END,f"id: {supplier[0]}, nome: {supplier[1]}, produto_fornecido: {supplier[2]}, quantia_mensal: {supplier[3]}, usuario: {supplier[4]}\n")