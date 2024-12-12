from fastapi import FastAPI, Path

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


@app.get("/user/{username}/{id}")
async def news(username: str = Path(min_length=3, max_length=15, description="Enter your username", example="montes")
               , id: int = Path(ge=0, le=100, description="Enter your id", example="75")) -> dict:
    return {"message": f"Hello, {username}:{id}"}


# Get - адрес в строке ?переменная=значение
# Post - формы (например оформить заказ в магазине)
# Put
# Delete
