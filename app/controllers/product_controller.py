from app.database.db_mysql import get_connection
from ..models.product_model import Product

def insert(product):
    try:
        conexion = get_connection()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO products (product_name, sku) VALUES (%s, %s)"
            val = (product.product_name, product.sku)
            cursor.execute(sql, val)
            conexion.commit()
            conexion.close()
        
    except Exception as ex:
        print(ex)
    
    return True

def get_product_by_sku(sku):
    try:
        conexion = get_connection()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM products WHERE sku = %s ",(sku))
            result = cursor.fetchone()
            product = Product(
                product_id = result[0],
                product_name = result[1], 
                sku = result[2],
                stock= result[3]
                )
            print (product.json())
            
    except Exception as ex:
        print(ex)

    return product


def select_all():
    conexion = get_connection()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        products = []
        for row in cursor.fetchall():
            product = Product(
                product_id = row[0],
                product_name = row[1], 
                sku = row[2],
                stock= row[3]
                )
            products.append(product)
    
    conexion.close()
    return products



