from flask_apscheduler import APScheduler
from app.services.inventory_service import InventoryService

scheduler = APScheduler()

@scheduler.task('interval', id='inventory_job', seconds=300)
def job():
    print ('inventory_job is running... ')
    products = InventoryService.get_inventories_out_stock()

    for product in products:

        if product.stock < 10:
            print ('inventario del producto SKU : {} casi se agota stock: {}'.format( product.sku, product.stock ))
    
    

