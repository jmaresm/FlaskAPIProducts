from app.controllers.product_controller import insert, select_all
from app.utils.Logger import Logger
import traceback
import json

class ProductService():

    def add_product(product):
        try:
            return insert(product)
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    def get_product_all():
        try:
            products = select_all()
            return products
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    

    