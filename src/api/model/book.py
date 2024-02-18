from pydantic import BaseModel

from src.api.model.author import Author
from src.api.model.category import Category


class Book(BaseModel):
    id: int


class BookCreate(Book):
    name: str
    category: Category
    author: Author
    description: str


class BookUpdate(Book):
    name: str
    category: Category
    author: Author
    description: str
