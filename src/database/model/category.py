from sqlalchemy import Column, Integer, String

from src.database.base import Base


class CategoryDB(Base):
    __tablename__ = 'category'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
