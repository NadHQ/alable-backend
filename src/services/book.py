from src.api.model.book import Book, BookCreate
from src.database.engine import async_session
from src.database.model.author import AuthorDB
from src.database.model.book import BookDB
from src.database.model.category import CategoryDB


class BookService:
    async def create_book(self, name: str, category: CategoryDB, author: AuthorDB, description: str) -> BookDB:
        async with async_session() as session:
            async with session.begin():
                book = BookCreate(name=name, category=category, author=author, description=description)
                await session.add(book.dict())
                await session.commit()
                return book
