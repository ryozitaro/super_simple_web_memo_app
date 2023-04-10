from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

import crud_memo as crud_memo
import schema_memo as schema_memo
from db import get_db

router = APIRouter()
# router.mount("/assets", StaticFiles(directory="assets"), name="assets")

templates = Jinja2Templates("templates")


""" 
@router.get("/memos", response_model=list[schema_memo.Memo])
async def list_memo(db: AsyncSession = Depends(get_db)):
    return await crud_memo.get_memos(db)
 """


@router.get("/", response_class=HTMLResponse)
async def list_memo(request: Request, db: AsyncSession = Depends(get_db)):
    memos_list = await crud_memo.get_memos(db)
    return templates.TemplateResponse(
        "sample.html", {"request": request, "item": {"memos_list": memos_list}}
    )


@router.post("/", response_model=schema_memo.MemoCreateResponse)
async def create_memo(
    memo_body: schema_memo.MemoCreate, db: AsyncSession = Depends(get_db)
):
    return await crud_memo.create_memo(db, memo_body)


@router.put("/{memo_id}", response_model=schema_memo.MemoCreateResponse)
async def update_memo(
    memo_id: int, memo_body: schema_memo.MemoCreate, db: AsyncSession = Depends(get_db)
):
    memo = await crud_memo.get_memo(db, memo_id)
    if memo is None:
        raise HTTPException(404, "Memo not found")

    return await crud_memo.update_memo(db, memo_body, memo)


@router.delete("/{memo_id}", response_model=None)
async def delete_memo(memo_id: int, db: AsyncSession = Depends(get_db)):
    memo = await crud_memo.get_memo(db, memo_id)
    if memo is None:
        raise HTTPException(404, "Memo not Found")

    return await crud_memo.delete_memo(db, memo)
