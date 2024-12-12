from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int
    completed: bool


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
    completed: bool
