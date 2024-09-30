from conftest import client

def test_get_products_all(client):
    response = client.get("/api/product/all")
    
    assert response.status_code == 200




