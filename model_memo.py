from sqlalchemy import Column, Integer, String
from db import Base


class Memo(Base):
    __tablename__ = "memos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
