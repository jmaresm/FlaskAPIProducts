

class Product():
    def __init__(self, product_id, product_name, sku, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.sku = sku
        self.stock = stock
    
    def json(self):
        return {'product_id': self.product_id, 'product_name': self.product_name, 'sku': self.sku, 'stock': self.stock}
    

class ProductRequest():
     def __init__(self, product_name, sku):
        self.product_name = product_name
        self.sku = sku
