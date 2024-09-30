from app.database.db_mysql import get_connection
from app.utils.Logger import Logger

def seed_test():
    print ('seed test....')
    try:
        conexion = get_connection()
        with conexion.cursor() as cursor:
            sql1= "INSERT INTO products (product_name, sku) VALUES ( %s, %s ); "
            sql2= "INSERT INTO products (product_name, sku) VALUES ( %s, %s ); "
            sql3= "INSERT INTO products (product_name, sku) VALUES ( %s, %s ); "
        
            cursor.execute(sql1, ('PRODUCT TESTING 1', 'test_xxx1'))
            cursor.execute(sql2, ('PRODUCT TESTING 2', 'test_xxx2'))
            cursor.execute(sql3, ('PRODUCT TESTING 3', 'test_xxx3'))
            
            conexion.commit()
            conexion.close()
    except Exception as ex:
        print(ex)
        Logger.add_to_log("error", ex)
    

def clean_test():
    try:
        conexion = get_connection()
        with conexion.cursor() as cursor:
            sql= "DELETE FROM products WHERE sku LIKE 'test%';"
            cursor.execute(sql)
            conexion.commit()
            conexion.close()
    except Exception as ex:
        print(ex)
        Logger.add_to_log("error", ex)