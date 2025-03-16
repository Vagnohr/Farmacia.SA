import tkinter as tk
from tkinter import messagebox
from crud_stuff_fornecedores import add_supplier, read_suppliers, update_supplier, delete_supplier

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FORNECEDORES")
        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Nome:").grid(row=0, column=0)
        tk.Label(self.root, text="Email:").grid(row=1, column=0)
        tk.Label(self.root, text="Produto Fornecido:").grid(row=2, column=0)
        tk.Label(self.root, text="Início do Contrato:").grid(row=3, column=0)
        tk.Label(self.root, text="Final do Contrato:").grid(row=4, column=0)
        tk.Label(self.root, text="Tipo de Transporte:").grid(row=5, column=0)
        tk.Label(self.root, text="Cidade:").grid(row=6, column=0)
        tk.Label(self.root, text="Estado:").grid(row=7, column=0)
        tk.Label(self.root, text="ID Fornecedor (for update/delete):").grid(row=8, column=0)

        # Entradas
        self.nome_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.produto_fornecido_entry = tk.Entry(self.root)
        self.inicio_contrato_entry = tk.Entry(self.root)
        self.final_contrato_entry = tk.Entry(self.root)
        self.tipo_transporte_entry = tk.Entry(self.root)
        self.cidade_entry = tk.Entry(self.root)
        self.estado_entry = tk.Entry(self.root)
        self.idfornecedor_entry = tk.Entry(self.root)

        # Posicionar entradas
        self.nome_entry.grid(row=0, column=1)
        self.email_entry.grid(row=1, column=1)
        self.produto_fornecido_entry.grid(row=2, column=1)
        self.inicio_contrato_entry.grid(row=3, column=1)
        self.final_contrato_entry.grid(row=4, column=1)
        self.tipo_transporte_entry.grid(row=5, column=1)
        self.cidade_entry.grid(row=6, column=1)
        self.estado_entry.grid(row=7, column=1)
        self.idfornecedor_entry.grid(row=8, column=1)

        # Botões
        tk.Button(self.root, text="Adicionar fornecedor", command=self.add_supplier).grid(row=9, column=0, columnspan=1)
        tk.Button(self.root, text="Listar fornecedores", command=self.read_suppliers).grid(row=9, column=1, columnspan=1)
        tk.Button(self.root, text="Alterar fornecedor", command=self.update_supplier).grid(row=10, column=0, columnspan=1)
        tk.Button(self.root, text="Excluir fornecedor", command=self.delete_supplier).grid(row=10, column=1, columnspan=1)

        self.text_area = tk.Text(self.root, height=10, width=80)
        self.text_area.grid(row=11, column=0, columnspan=4)

    def add_supplier(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        produto_fornecido = self.produto_fornecido_entry.get()
        inicio_contrato = self.inicio_contrato_entry.get()
        final_contrato = self.final_contrato_entry.get()
        transporte = self.tipo_transporte_entry.get()
        cidade = self.cidade_entry.get()
        estado = self.estado_entry.get()

        if nome and email and produto_fornecido and inicio_contrato and final_contrato and transporte and cidade and estado:
            add_supplier(nome, email, produto_fornecido, inicio_contrato, final_contrato, transporte, cidade, estado)
            self.clear_entries()
            messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")

    def read_suppliers(self):
        suppliers = read_suppliers()
        self.text_area.delete(1.0, tk.END)
        for supplier in suppliers:
            self.text_area.insert(tk.END, f"id: {supplier[0]}, nome: {supplier[1]}, email: {supplier[2]}, produto: {supplier[3]}, "
                                           f"início contrato: {supplier[4]}, final contrato: {supplier[5]}, transporte: {supplier[6]}, "
                                           f"cidade: {supplier[7]}, estado: {supplier[8]}\n")

    def update_supplier(self):
        idfornecedor = self.idfornecedor_entry.get()
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        produto_fornecido = self.produto_fornecido_entry.get()
        inicio_contrato = self.inicio_contrato_entry.get()
        final_contrato = self.final_contrato_entry.get()
        transporte = self.tipo_transporte_entry.get()
        cidade = self.cidade_entry.get()
        estado = self.estado_entry.get()

        if idfornecedor and nome and email and produto_fornecido and inicio_contrato and final_contrato and transporte and cidade and estado:
            update_supplier(idfornecedor, nome, email, produto_fornecido, inicio_contrato, final_contrato, transporte, cidade, estado)
            self.clear_entries()
            messagebox.showinfo("Sucesso", "Fornecedor alterado com sucesso")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")

    def delete_supplier(self):
        supplier_id = self.idfornecedor_entry.get()
        if supplier_id:
            delete_supplier(supplier_id)
            self.idfornecedor_entry.delete(0, tk.END)
            messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso")
        else:
            messagebox.showerror("Erro", "ID do fornecedor é obrigatório")

    def clear_entries(self):
        """Limpa todas as entradas após uma operação"""
        self.nome_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.produto_fornecido_entry.delete(0, tk.END)
        self.inicio_contrato_entry.delete(0, tk.END)
        self.final_contrato_entry.delete(0, tk.END)
        self.tipo_transporte_entry.delete(0, tk.END)
        self.cidade_entry.delete(0, tk.END)
        self.estado_entry.delete(0, tk.END)
        self.idfornecedor_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
