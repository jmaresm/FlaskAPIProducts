from app.database.db_mysql import get_connection
from app.models.product_model import Product

def add_inventory(id, stock):
    try:

        conexion = get_connection()
        with conexion.cursor() as cursor:
            sql = "UPDATE products SET stock = %s WHERE product_id = %s "
            val = (stock, id)
            cursor.execute(sql, val)
            conexion.commit()
            conexion.close()
        
    except Exception as ex:
        print(ex)
    
    return True

def get_out_stock():
    conexion = get_connection()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM products WHERE stock < 10")
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