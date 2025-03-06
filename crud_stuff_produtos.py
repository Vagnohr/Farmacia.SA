import mysql.connector
MYSQL_HOST='localhost'
MYSQL_USER='root'
MYSQL_PASSWORD=''
MYSQL_DATABASE='produtos'
def get_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE)
def add_product(nome,estoque,valor,usuario):
    conn=get_connection()
    cursor=conn.cursor()
    query="insert produtos(nome,estoque,valor,usaurio)VALUES(%s,%i,%d,%s)"
    cursor.execute(query,(nome,estoque,valor,usuario))
    conn.commit()
    cursor.close()
    conn.close()
def read_products():
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT * FROM produtos"
    cursor.execute(query) 
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def update_product(nome,estoque,valor):
    conn=get_connection()
    cursor=conn.cursor()
    query="UPDATE produtos SET nome=%s,estoque=%i,valor=%d WHERE idproduto=%s"
    cursor.execute(query,(nome,estoque,valor))
    conn.commit()
    cursor.close()
    conn.close()
def delete_product(product_id):
    conn=get_connection()
    cursor=conn.cursor()
    query="DELETE FROM produtos WHERE idproduto=%s"
    cursor.execute(query,(product_id,))
    conn.commit()
    cursor.close()
    conn.close()