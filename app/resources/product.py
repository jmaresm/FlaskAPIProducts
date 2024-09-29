from flask import Blueprint, request, abort
from flask_restful import Resource, Api
from app.services.product_service import ProductService
from app.utils.Logger import Logger
from app.models.product_model import ProductRequest


main = Blueprint('product_blueprint', __name__)

api = Api()

class ProductResource(Resource):
    
    def post(self):
        if not request.json:
            abort(415)
        try:
            product = ProductRequest(
                product_name = request.json["product_name"],
                sku= request.json["sku"])
            result = ProductService.add_product(product)
            if result :
                return {'result': 'Producto agregado correctamente'}, 201
        except Exception as ex:
            Logger.add_to_log("error", str(ex))

    def get(self):
        results = ProductService.get_product_all()
        products = [ product.json() for product in results ]
        return {'results': products }
    

api.add_resource(ProductResource, '/api/product' , '/api/product/all')

