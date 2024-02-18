from sqlalchemy import Column, Integer, String, ForeignKey, Text

from src.database.base import Base


class BookDB(Base):
    __tablename__ = 'book'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String())
    category = Column(ForeignKey('category.id'), nullable=False)
    author = Column(ForeignKey('author.id'), nullable=False)
    description = Column(Text())
