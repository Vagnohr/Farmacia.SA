import tkinter as tk
from tkinter import messagebox
from crud_stuff_produtos import create_product,read_products,update_product,delete_product
class CRUDApp:
    def __init__(self,root):
        self.root=root
        self.root.title("CRUD PRODUTOS")
        #criação de widgets
        self.create_widgets()
    def create_widgets(self):
        #Labels
        tk.Label(self.root,text="Nome:").grid(row=0,column=0)
        tk.Label(self.root,text="Etoque:").grid(row=1,column=0)
        tk.Label(self.root,text="Valor:").grid(row=2,column=0)
        tk.Label(self.root,text="Id Produto (for update/delete):").grid(row=3,column=0)
        #criar as caixas para digitar os valores
        self.nome_entry=tk.Entry(self.root)
        self.estoque_entry=tk.Entry(self.root)
        self.valor_entry=tk.Entry(self.root)
        self.idproduto_entry=tk.Entry(self.root)
        self.nome_entry.grid(row=0,column=1)
        self.estoque_entry.grid(row=1,column=1)
        self.valor_entry.grid(row=2,column=1)
        self.idproduto_entry.grid(row=3,column=1)
        #botões do crud
        tk.Button(self.root,text="Criar produto",command=self.create_product).grid(row=5,column=0,columnspan=1)
        tk.Button(self.root,text="Listar produtos",command=self.read_products).grid(row=5,column=1,columnspan=1)
        tk.Button(self.root,text="Alterar produtos",command=self.update_product).grid(row=6,column=0,columnspan=1)
        tk.Button(self.root,text="Excluir produtos",command=self.delete_product).grid(row=6,column=1,columnspan=1)
        self.text_area=tk.Text(self.root,height=10,width=80)
        self.text_area.grid(row=10,column=0,columnspan=4)
    def create_product(self):
        nome=self.nome_entry.get()
        telefone=self.estoque_entry.get()
        email=self.valor_entry.get()
        if nome and telefone and email:
            create_product(nome,telefone,email)
            self.nome_entry.delete(0,tk.END)
            self.estoque_entry.delete(0,tk.END)
            self.valor_entry.delete(0,tk.END)
            messagebox.showinfo("Successo","Produto criado com sucesso")
        else:
            messagebox.showerror("Error","Todos os campos são obrigatórios")
    def read_products(self):
        products=read_products()
        self.text_area.delete(1.0,tk.END)
        for product in products:
            self.text_area.insert(tk.END,f"id: {product[0]}, nome: {product[1]}, telefone: {product[2]}, email: {product[3]}\n")
    def update_product(self):
        idproduto=self.idproduto_entry.get()
        nome=self.nome_entry.get()
        estoque=self.estoque_entry.get()
        valor=self.valor_entry.get()
        if idproduto and nome and estoque and valor:
            update_product(idproduto,nome,estoque,valor)
            self.nome_entry.delete(0,tk.END)
            self.estoque_entry.delete(0,tk.END)
            self.valor_entry.delete(0,tk.END)
            self.idproduto_entry.delete(0,tk.END)
            messagebox.showinfo("Successo","Produto alterado com sucesso")
        else:
            messagebox.showerror("Error","Todos os campos são obrigatórios")
    def delete_product(self):
        user_id=self.idproduto_entry.get()
        if user_id:
            delete_product(user_id)
            self.idproduto_entry.delete(0,tk.END)
            messagebox.showinfo("Success","Produto excluido com sucesso")
        else:
            messagebox.showerror("Error","ID do produto é obrigatório")
if __name__=="__main__":
    root=tk.Tk()
    app=CRUDApp(root)
    root.mainloop()