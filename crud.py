from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError, PyMongoError
from user_crud_api.database import collection  # type: ignore
from user_crud_api.models import UserCreate  # type: ignore


def create_user(user: UserCreate):
    existing = collection.find_one({"phone": user.phone})
    if existing:
        return "User already exists."
    collection.insert_one(user.dict())
    return {"message": "User created successfully"}


def get_user(phone):
    user = collection.find_one({"phone": phone})
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    user["_id"] = str(user["_id"])  # Convert ObjectId to string
    return user


def update_user_put(phone, data):
    result = collection.update_one({"phone": phone}, {"$set": {
        "name": data.name, "serial_no": [data.serial_no]
    }})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": "User updated (PUT)."}


def update_user_push(phone, data):
    result = collection.update_one({"phone": phone}, {"$push": {
        "serial_no": data.serial_no
    }})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": "Serial number added (PUSH)."}


def delete_user(phone):
    result = collection.delete_one({"phone": phone})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": "User deleted successfully."}
