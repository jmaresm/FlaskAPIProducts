from app.controllers.inventory_controller import add_inventory, get_out_stock
from app.utils.Logger import Logger
import traceback

class InventoryService():
    def add_inventory(id, stock):
        try: 
            return add_inventory(id, stock)
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        
    def get_inventories_out_stock():
        try:
            products = get_out_stock()
            return products
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

