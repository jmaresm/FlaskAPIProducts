from conftest import client

def test_add_inventory(client):

    product_id = 1
    response = client.patch(
        "api/inventories/product/{}".format(product_id), 
        json={"stock": 10}
        )
    
    assert response.status_code == 200
