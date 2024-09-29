from app.models.order_request import Order

def convertToObject(json):
    orders = []
    for order in json["orders"]:
        orders.append(
            Order(sku = order["sku"], 
                    amount = order["amount"])
        )
        
    return orders