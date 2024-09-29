from flask import Blueprint, request, abort
from flask_restful import Resource, Api
from app.utils.Logger import Logger
from app.utils.mapper import convertToObject
from app.services.order_service import OrderService   

main = Blueprint('order_blueprint', __name__)

api = Api()

class OrderResource(Resource):
    def post(self):
        if not request.json:
            abort(415)
        try:
            orders = convertToObject(request.json)

            result = OrderService.create(orders)

            if result :
                 return {'result': 'Order colocada correctamente'}, 200
            
        except Exception as ex:
            Logger.add_to_log("error", str(ex))

    

api.add_resource(OrderResource, '/api/orders' )
