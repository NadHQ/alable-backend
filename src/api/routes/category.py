from fastapi import APIRouter

from src.api.model.book import BookCreate
from src.services.book import BookService

book_router = APIRouter()

book_service = BookService()


@book_router.post("/create_book/", response_model=BookCreate)
async def create_book(book: BookCreate):
    await book_service.create_book(**book)
