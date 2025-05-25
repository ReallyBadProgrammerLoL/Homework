import requests

BASE_URL = "http://127.0.0.1:8000/api/products"

def test_get_all():
    print("GET /products")
    response = requests.get(BASE_URL)
    print(response.status_code, response.json())

def test_create_product():
    print("POST /products")
    product = {"name": "Сыр гауда", "price": 230.50}
    response = requests.post(BASE_URL, json=product)
    print(response.status_code, response.json())
    return response.json()["id"]


def test_get_product(product_id):
    print(f"GET /products/{product_id}")
    response = requests.get(f"{BASE_URL}/{product_id}")
    print(response.status_code, response.json())

def test_update_product(product_id):
    print("PUT /products")
    updated = {"id": product_id, "name": "Сыр гауда 45%", "price": 250.00}
    response = requests.put(BASE_URL, json=updated)
    print(response.status_code, response.json())


def test_delete_product(product_id):
    print(f"DELETE /products/{product_id}")
    response = requests.delete(f"{BASE_URL}/{product_id}")
    print(response.status_code, response.json())

if __name__ == "__main__":
    test_get_all()
    new_id = test_create_product()
    test_get_product(new_id)
    test_update_product(new_id)
    test_get_product(new_id)
    test_delete_product(new_id)
    test_get_product(new_id)
