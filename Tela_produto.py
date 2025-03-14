import tkinter as tk
from tkinter import messagebox
from crud_stuff_produtos import add_product, read_products

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PRODUTOS")
        # criação de widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Nome:").grid(row=0, column=0)
        tk.Label(self.root, text="Estoque:").grid(row=1, column=0)  # Corrigido
        tk.Label(self.root, text="Valor:").grid(row=2, column=0)
        tk.Label(self.root, text="Descrição:").grid(row=3, column=0)
        tk.Label(self.root, text="Validade:").grid(row=4, column=0)
        tk.Label(self.root, text="Usuário:").grid(row=5, column=0)
        tk.Label(self.root, text="Id Produto (for update/delete):").grid(row=6, column=0)

        # Entradas
        self.nome_entry = tk.Entry(self.root)
        self.estoque_entry = tk.Entry(self.root)
        self.valor_entry = tk.Entry(self.root)
        self.descricao_entry = tk.Entry(self.root)
        self.validade_entry = tk.Entry(self.root)
        self.usuario_entry = tk.Entry(self.root)
        self.idproduto_entry = tk.Entry(self.root)
        self.nome_entry.grid(row=0, column=1)
        self.estoque_entry.grid(row=1, column=1)
        self.valor_entry.grid(row=2, column=1)
        self.descricao_entry.grid(row=3, column=1)
        self.validade_entry.grid(row=4, column=1)
        self.usuario_entry.grid(row=5, column=1)
        self.idproduto_entry.grid(row=6, column=1)

        # Botões do CRUD
        tk.Button(self.root, text="Adicionar produto", command=self.add_product).grid(row=7, column=0, columnspan=1)
        tk.Button(self.root, text="Listar produtos", command=self.read_products).grid(row=7, column=1, columnspan=1)
        tk.Button(self.root, text="Alterar produtos", command=self.update_product).grid(row=8, column=0, columnspan=1)
        tk.Button(self.root, text="Excluir produtos", command=self.delete_product).grid(row=8, column=1, columnspan=1)

        self.text_area = tk.Text(self.root, height=10, width=80)
        self.text_area.grid(row=9, column=0, columnspan=4)

    def add_product(self):
        nome = self.nome_entry.get()
        estoque = self.estoque_entry.get()
        valor = self.valor_entry.get()
        usuario = self.usuario_entry.get()
        descricao = self.descricao_entry.get()
        validade = self.validade_entry.get()
        if nome and estoque and valor and usuario and descricao and validade:
            add_product(nome, estoque, valor)
            self.nome_entry.delete(0, tk.END)
            self.estoque_entry.delete(0, tk.END)
            self.valor_entry.delete(0, tk.END)
            self.usuario_entry.delete(0, tk.END)
            self.descricao_entry.delete(0, tk.END)
            self.validade_entry.delete(0, tk.END)
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")

    def read_products(self):
        products = read_products()
        self.text_area.delete(1.0, tk.END)
        for product in products:
            self.text_area.insert(
                tk.END, 
                f"id: {product[0]}, nome: {product[1]}, estoque: {product[2]}, valor: {product[3]}, descrição: {product[4]}, validade: {product[5]}, usuário: {product[6]}\n"
            )

    # Métodos ausentes
    def update_product(self):
        messagebox.showinfo("Info", "Função de atualizar produto ainda não implementada")

    def delete_product(self):
        messagebox.showinfo("Info", "Função de excluir produto ainda não implementada")

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
