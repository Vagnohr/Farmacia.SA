import tkinter as tk
from tkinter import messagebox
from crud_stuff_fornecedores import add_supplier, read_suppliers

class TelaFornecedor:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Fornecedores")
        self.create_widgets()

    def create_widgets(self):
        # Labels e campos de entrada
        labels = [
            "Nome", "Email", "Produto Fornecido", 
            "Tipo de Transporte", "Cidade", "Estado"
        ]
        self.entries = []
        for i, text in enumerate(labels):
            tk.Label(self.root, text=f"{text}:").grid(row=i, column=0)
            entry = tk.Entry(self.root)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

        # Botões para operações
        tk.Button(self.root, text="Adicionar Fornecedor", command=self.add_supplier).grid(row=6, column=0)
        tk.Button(self.root, text="Listar Fornecedores", command=self.list_suppliers).grid(row=6, column=1)

        # Área de texto para exibir os fornecedores
        self.text_area = tk.Text(self.root, height=10, width=80)
        self.text_area.grid(row=7, column=0, columnspan=2)

    def add_supplier(self):
        # Obtém dados dos campos
        fields = [entry.get() for entry in self.entries]
        if all(fields):  # Certifica-se de que todos os campos foram preenchidos
            try:
                add_supplier(*fields)  # Passa os dados para o CRUD
                messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")
                self.clear_entries()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar fornecedor: {e}")
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    def list_suppliers(self):
        try:
            suppliers = read_suppliers()
            self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
            if suppliers:
                for supplier in suppliers:
                    self.text_area.insert(
                        tk.END,
                        f"ID: {supplier[0]}, Nome: {supplier[1]}, Email: {supplier[2]}, "
                        f"Produto: {supplier[3]}, Transporte: {supplier[4]}, Cidade: {supplier[5]}, Estado: {supplier[6]}\n"
                    )
            else:
                self.text_area.insert(tk.END, "Nenhum fornecedor encontrado.\n")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao listar fornecedores: {e}")

    def clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaFornecedor(root)
    root.mainloop()
