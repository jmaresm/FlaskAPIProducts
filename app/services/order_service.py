from app.controllers.order_controller import set_order
from app.controllers.product_controller import get_product_by_sku
from app.database.db_mysql import get_connection
from app.utils.Logger import Logger
from app.models.order_request import Order
import traceback

class OrderService():
    def create(orders : list[Order]): 
        try: 
            for order in orders:
                product = get_product_by_sku(order.sku)

                if product:
                    newStock = product.stock - order.amount
                    if newStock > 0:
                        set_order(order.sku, newStock)
                    else:
                        raise  Exception('Inventario insuficiente producto [{}]'.format(order.sku))
                else:
                    raise Exception('Producto no enconstrado {}'.format(order.sku))
            
            
            db = get_connection()
            db.commit()
            db.close()

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            

        return True