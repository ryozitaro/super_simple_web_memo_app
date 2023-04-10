from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import model_memo as model_memo
import schema_memo as schema_memo


async def create_memo(
    db: AsyncSession, memo_body: schema_memo.MemoCreate
) -> model_memo.Memo:
    memo = model_memo.Memo(text=memo_body.text)
    db.add(memo)
    await db.commit()
    await db.refresh(memo)
    return memo


async def get_memos(db: AsyncSession) -> list[schema_memo.Memo]:
    result: Result = await db.execute(select(model_memo.Memo.id, model_memo.Memo.text))
    return result.all()[::-1]


async def get_memo(db: AsyncSession, memo_id: int) -> model_memo.Memo | None:
    result: Result = await db.execute(
        select(model_memo.Memo).filter(model_memo.Memo.id == memo_id)
    )
    memo: tuple[model_memo.Memo] | None = result.first()
    return memo[0] if memo is not None else None


async def update_memo(
    db: AsyncSession, create_memo: schema_memo.MemoCreate, original: model_memo.Memo
) -> model_memo.Memo:
    original.text = create_memo.text
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_memo(db: AsyncSession, original: model_memo.Memo) -> None:
    await db.delete(original)
    await db.commit()
