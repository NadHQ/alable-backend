import os

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/asyncalchemy"
DATABASE_URL = config('DATABASE_URL')
engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
