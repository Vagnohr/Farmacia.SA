import mysql.connector

# Configurações do banco de dados
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''  # Substitua pelo seu password, se necessário
MYSQL_DATABASE = 'farmacia_sa'

def get_connection():
    """Estabelece conexão com o banco de dados"""
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

# Adicionar fornecedor
def add_supplier(nome, email, produto, transporte, cidade, estado):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """INSERT INTO fornecedor (nome, email, produto, transporte, cidade, estado)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (nome, email, produto, transporte, cidade, estado))
        conn.commit()
        print("Fornecedor adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar fornecedor: {e}")
    finally:
        cursor.close()
        conn.close()

# Ler todos os fornecedores
def read_suppliers():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM fornecedor"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Erro ao listar fornecedores: {e}")
    finally:
        cursor.close()
        conn.close()

# Atualizar fornecedor
def update_supplier(idfornecedor, nome, email, produto, transporte, cidade, estado):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """UPDATE fornecedor SET nome = %s, email = %s, produto = %s, 
                   transporte = %s, cidade = %s, estado = %s WHERE idfornecedor = %s"""
        cursor.execute(query, (nome, email, produto, transporte, cidade, estado, idfornecedor))
        conn.commit()
        print("Fornecedor atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar fornecedor: {e}")
    finally:
        cursor.close()
        conn.close()

# Deletar fornecedor
def delete_supplier(idfornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM fornecedor WHERE idfornecedor = %s"
        cursor.execute(query, (idfornecedor,))
        conn.commit()
        print("Fornecedor deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar fornecedor: {e}")
    finally:
        cursor.close()
        conn.close()

# *** Funcionalidades adicionais (do meu CRUD) ***

# Listar todos os fornecedores com menos detalhes
def listar_todos_os_fornecedores():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT idfornecedor, nome, email, cidade, estado FROM fornecedor"
        cursor.execute(query)
        result = cursor.fetchall()
        for fornecedor in result:
            print(f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Email: {fornecedor[2]}, Cidade: {fornecedor[3]}, Estado: {fornecedor[4]}")
    except Exception as e:
        print(f"Erro ao listar todos os fornecedores: {e}")
    finally:
        cursor.close()
        conn.close()

# Buscar fornecedor por nome
def buscar_fornecedor_por_nome(nome):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM fornecedor WHERE nome LIKE %s"
        cursor.execute(query, (f"%{nome}%",))
        result = cursor.fetchall()
        for fornecedor in result:
            print(f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Email: {fornecedor[2]}, Produto: {fornecedor[3]}, Transporte: {fornecedor[4]}, Cidade: {fornecedor[5]}, Estado: {fornecedor[6]}")
    except Exception as e:
        print(f"Erro ao buscar fornecedor por nome: {e}")
    finally:
        cursor.close()
        conn.close()
