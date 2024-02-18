from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.database.base import Base


class AuthorDB(Base):
    __tablename__ = 'author'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String())
