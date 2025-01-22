from fastapi import APIRouter, Depends
from auth.auth_handler import verify_admin_role
from auth.auth_bearer import JWTBearer
from core.database import db

router = APIRouter()

@router.post("/add", dependencies=[Depends(JWTBearer())])
async def add_data(data: dict, token: str = Depends(JWTBearer())):
    verify_admin_role(token)
    result = await db.general.insert_one(data)
    return {"message": "Data added successfully"}
