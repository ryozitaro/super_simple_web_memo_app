from pydantic import BaseModel, Field


class MemoBase(BaseModel):
    text: str | None = Field(default=None)


class MemoCreate(MemoBase):
    pass


class MemoCreateResponse(MemoCreate):
    id: int

    class Config:
        orm_mode = True


class Memo(MemoBase):
    id: int

    class Config:
        orm_mode = True
