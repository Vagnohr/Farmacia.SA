import mysql.connector
MYSQL_HOST='localhost'
MYSQL_USER='root'
MYSQL_PASSWORD=''
MYSQL_DATABASE='farmacia_sa'
def get_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE)
def add_supplier(nome,produto_fornecido,quantia_mensal,usuario):
    conn=get_connection()
    cursor=conn.cursor()
    query="insert fornecedor(nome,produto_fornecio,quantia_mensal,usuario)VALUES(%s,%s,%i,%s)"
    cursor.execute(query,(nome,produto_fornecido,quantia_mensal,usuario))
    conn.commit()
    cursor.close()
    conn.close()
def read_suppliers():
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT * FROM fornecedor"
    cursor.execute(query) 
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def update_supplier(nome,produto_fornecido,quantia_mensal):
    conn=get_connection()
    cursor=conn.cursor()
    query="UPDATE produtos SET nome=%s,produto_fornecido=%s,quantia_mensal=%i WHERE idfornecedor=%s"
    cursor.execute(query,(nome,produto_fornecido,quantia_mensal))
    conn.commit()
    cursor.close()
    conn.close()
def delete_supplier(supplier_id):
    conn=get_connection()
    cursor=conn.cursor()
    query="DELETE FROM fornecedor WHERE idfornecedor=%s"
    cursor.execute(query,(supplier_id))
    conn.commit()
    cursor.close()
    conn.close()