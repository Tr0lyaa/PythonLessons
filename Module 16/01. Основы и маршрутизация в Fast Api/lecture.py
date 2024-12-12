from fastapi import FastAPI

# FastAPI - фреймворк
# Инициализация приложения
app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello world"}


@app.get("/user/A/B")
async def news() -> dict:
    return {"message": f"Hello, Tester"}


@app.get("/id")
async def id_paginator(username: str = "Tolya", age: int = 27) -> dict:
    return {"User": username, "Age": age}


@app.get("/user/{first_name}/{last_name}")
async def news(first_name: str, last_name: str) -> dict:
    return {"message": f"Hello, {first_name} {last_name}"}


# Get - адрес в строке ?переменная=значение
# Post - формы (например оформить заказ в магазине)
# Put
# Delete
