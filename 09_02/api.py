import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse
from typing import Optional


class Product:
    def __init__(self, name: str, price: float):
        self.id = str(uuid.uuid4())
        self.name = name.strip()
        self.price = price

products = [
    Product("Хлеб подовый", 45.50),
    Product("Молоко 2,5%", 80.20),
    Product("Яйца куриные 10шт", 120.00),
    Product("Сахар 1кг", 65.30),
    Product("Масло сливочное", 150.75)
]

def find_product(id: str) -> Optional[Product]:
    for product in products:
        if product.id == id:
            return product
    return None

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Добро пожаловать в продуктовый API"}

@app.get("/api/products")
async def get_products():
    return products

@app.get("/api/products/{id}")
async def get_product(id: str):
    product = find_product(id)
    if product is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Товар не найден"}
        )
    return product

@app.post("/api/products")
async def create_product(data: dict = Body(...)):
    product = Product(data["name"], data["price"])
    products.append(product)
    return product

@app.put("/api/products")
async def edit_product(data: dict = Body(...)):
    product = find_product(data["id"])
    if product is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Товар не найден"}
        )
    product.name = data["name"]
    product.price = data["price"]
    return product

@app.delete("/api/products/{id}")
async def delete_product(id: str):
    product = find_product(id)
    if product is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Товар не найден"}
        )
    products.remove(product)
    return product
