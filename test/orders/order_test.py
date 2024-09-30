from app.controllers.test_controller import seed_test


def test_create_orders(client):
    
    #seed_test()
    
    body = {
        "orders" : [
            {
                "sku": "test_xxx1",
                "amount": 34
            },
            {
                "sku": "test_xxx2",
                "amount": 12
            }
        ]
    }
    
    response = client.post('api/orders', json = body)
    
    assert response.status_code == 200 
    
    
    
    