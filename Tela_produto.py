import tkinter as tk
from tkinter import messagebox
from crud_stuff_produtos import add_product, read_products  # Importa as funções do CRUD

class ProductApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Produtos")
        self.create_widgets()

    def create_widgets(self):
        # Labels e Entradas
        tk.Label(self.root, text="Nome do Produto:").grid(row=0, column=0)
        tk.Label(self.root, text="Fornecedor:").grid(row=1, column=0)
        tk.Label(self.root, text="Quantidade:").grid(row=2, column=0)
        tk.Label(self.root, text="Valor:").grid(row=3, column=0)
        tk.Label(self.root, text="Validade (DD-MM-AAAA):").grid(row=4, column=0)
        tk.Label(self.root, text="Descrição:").grid(row=5, column=0)
        tk.Label(self.root, text="ID:").grid(row=6, column=0)

        self.nome_entry = tk.Entry(self.root)
        self.fornecedor_entry = tk.Entry(self.root)
        self.quantidade_entry = tk.Entry(self.root)
        self.valor_entry = tk.Entry(self.root)
        self.validade_entry = tk.Entry(self.root)
        self.descricao_entry = tk.Entry(self.root)
        self.id_entry = tk.Entry(self.root)

        self.nome_entry.grid(row=0, column=1)
        self.fornecedor_entry.grid(row=1, column=1)
        self.quantidade_entry.grid(row=2, column=1)
        self.valor_entry.grid(row=3, column=1)
        self.validade_entry.grid(row=4, column=1)
        self.descricao_entry.grid(row=5, column=1)
        self.id_entry.grid(row=6, column=1)

        # Botões
        tk.Button(self.root, text="Adicionar Produto", command=self.add_product).grid(row=7, column=0)
        tk.Button(self.root, text="Listar Produtos", command=self.list_products).grid(row=7, column=1)

        # Área de texto para exibir produtos
        self.text_area = tk.Text(self.root, height=15, width=50)
        self.text_area.grid(row=8, column=0, columnspan=3)

    def add_product(self):
        nome = self.nome_entry.get()
        fornecedor = self.fornecedor_entry.get()
        quantidade = self.quantidade_entry.get()
        valor = self.valor_entry.get()
        validade = self.validade_entry.get()
        descricao = self.descricao_entry.get()

        if nome and fornecedor and quantidade and valor and validade and descricao:
            try:
                # Chamada para o CRUD
                add_product(nome, quantidade, valor, fornecedor, descricao, validade)
                self.nome_entry.delete(0, tk.END)
                self.fornecedor_entry.delete(0, tk.END)
                self.quantidade_entry.delete(0, tk.END)
                self.valor_entry.delete(0, tk.END)
                self.validade_entry.delete(0, tk.END)
                self.descricao_entry.delete(0, tk.END)
                messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar o produto: {e}")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

    def list_products(self):
        try:
            # Obtém os produtos do CRUD
            products = read_products()
            self.text_area.delete(1.0, tk.END)

            if products:
                for product in products:
                    self.text_area.insert(
                        tk.END,
                        f"ID: {product[0]}\nNome: {product[1]}\nValor: {product[2]}\n"
                        f"Fornecedor: {product[3]}\nDescrição: {product[4]}\nValidade: {product[5]}\n"
                        f"Quantidade: {product[6]}\n{'-'*30}\n"
                    )
            else:
                self.text_area.insert(tk.END, "Nenhum produto encontrado.\n")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao listar os produtos: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductApp(root)
    root.mainloop()
