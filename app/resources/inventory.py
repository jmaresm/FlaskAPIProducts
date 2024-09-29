from flask import Blueprint, request, abort
from flask_restful import Resource, Api
from app.services.inventory_service import add_inventory
from app.utils.Logger import Logger


main = Blueprint('inventory_blueprint', __name__)

api = Api()

class InventoryResource(Resource):
    def patch(self,id):
        if not request.json:
            abort(415)
        try:
            
            result = add_inventory(id, request.json["stock"]) 
            
            if result :
                return {'result': 'Inventario agregado correctamente'}, 200
            
        except Exception as ex:
            Logger.add_to_log("error", str(ex))

    

api.add_resource(InventoryResource, '/api/inventories/product/<int:id>' )

