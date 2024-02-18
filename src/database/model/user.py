from sqlalchemy import Column, Integer, String

from src.database.base import Base


class UserDB(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    password = Column(String())
    email = Column(String())
