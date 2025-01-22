from fastapi import APIRouter
from core.database import db

router = APIRouter()

@router.get("/")
async def get_all_data(collection: str):
    data = await db[collection].find().to_list(100)
    return data
