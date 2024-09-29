from app.database.db_mysql import get_connection

def set_order(sku, stock):
    try:
        conexion = get_connection()
        with conexion.cursor() as cursor:
            sql = "UPDATE products SET stock = %s WHERE sku = %s"
            val = (stock, sku)
            cursor.execute(sql, val)
            
        conexion.commit()
    except Exception as ex:
        print(ex)