from pydantic import BaseModel
from pydantic import EmailStr


class User(BaseModel):
    id: int


class UserCreate(User):
    email: EmailStr
    password: str


class UserUpdate(User):
    email: EmailStr
    password: str
