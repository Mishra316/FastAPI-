from pydantic import BaseModel
from typing import List


class UserCreate(BaseModel):
    name: str
    phone: str
    serial_no: str


class UserUpdatePut(BaseModel):
    name: str
    serial_no: str


class UserPushSerial(BaseModel):
    serial_no: str
