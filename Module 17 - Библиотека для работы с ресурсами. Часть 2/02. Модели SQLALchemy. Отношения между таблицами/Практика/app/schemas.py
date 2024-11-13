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
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateTask(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
