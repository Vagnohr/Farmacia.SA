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
def add_product(nome,estoque,valor,descricao,validade,usuario):
    conn=get_connection()
    cursor=conn.cursor()
    query="insert produto(nome,estoque,valor,descricao,validade,usuario)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(nome,estoque,valor,descricao,validade,usuario))
    conn.commit()
    cursor.close()
    conn.close()
def read_products():
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT * FROM produto"
    cursor.execute(query) 
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def update_product(nome,estoque,valor,descricao,validade):
    conn=get_connection()
    cursor=conn.cursor()
    query="UPDATE produto SET nome=%s,estoque=%s,valor=%s,descrição=%s,validade=%s, WHERE idproduto=%s"
    cursor.execute(query,(nome,estoque,valor,descricao,validade))
    conn.commit()
    cursor.close()
    conn.close()
def delete_product(product_id):
    conn=get_connection()
    cursor=conn.cursor()
    query="DELETE FROM produto WHERE idproduto=%s"
    cursor.execute(query,(product_id,))
    conn.commit()
    cursor.close()
    conn.close()