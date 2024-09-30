from conftest import client

def test_add_product(client):
    

    response = client.post("api/product", json= {
        "product_name": "TEST PRODUCT",
        "sku": "test_XXXXXX"
    })

    assert response.status_code == 201
    
    