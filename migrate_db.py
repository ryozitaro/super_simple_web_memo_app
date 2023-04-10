from sqlalchemy import create_engine

from model_memo import Base


DB_PATH = "sqlite:///memo.sqlite3"
engine = create_engine(DB_PATH, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
