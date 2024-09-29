class Order():
    
    def __init__ (self, sku, amount):
        self.sku = sku
        self.amount = amount

    def json(self):
        return {'sku': self.sku, 'amount': self.amount}



