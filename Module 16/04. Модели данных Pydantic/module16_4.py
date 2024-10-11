from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")]
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]


@app.get("/users")
async def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def new_user(user: User) -> str:
    user.id = 1 if len(users) == 0 else users[-1].id + 1
    users.append(user)
    return f"User {user.id} is registered."


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]
                      , username: Annotated[str, Path(min_length=5, max_length=20,
                                                      description="Enter username", example="UrbanUser")]
                      , age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    for i in range(len(users)):
        if users[i].id == user_id:
            edit_user = users[i]
            edit_user.username = username
            edit_user.age = age
            return f"User {user_id} has been updated."
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]) -> str:
    for i in range(len(users)):
        if users[i].id == user_id:
            users.pop(i)
            return f"User {user_id} has been deleted."

    raise HTTPException(status_code=404, detail="User was not found")
