from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_PATH = "sqlite+aiosqlite:///memo.sqlite3"

engine = create_async_engine(url=DB_PATH, echo=True)

Session = sessionmaker(bind=engine, autoflush=False, class_=AsyncSession)

Base = declarative_base()


async def get_db():
    async with Session() as session:
        yield session
