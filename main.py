from fastapi import FastAPI, HTTPException
from .models import UserCreate, UserUpdatePut, UserPushSerial

from . import crud

app = FastAPI(title="User CRUD API with MongoDB")


@app.post("/users/create")
def create_user(user: UserCreate):
    result = crud.create_user(user)
    if result == "User already exists.":
        raise HTTPException(status_code=400, detail="User already exists.")
    return result


@app.get("/users/{phone}")
def read_user(phone: str):
    return crud.get_user(phone)


@app.put("/users/{phone}")
def update_user_put(phone: str, data: UserUpdatePut):
    return crud.update_user_put(phone, data)


@app.patch("/users/{phone}")
def update_user_push(phone: str, data: UserPushSerial):
    return crud.update_user_push(phone, data)


@app.delete("/users/{phone}")
def delete_user(phone: str):
    return crud.delete_user(phone)
