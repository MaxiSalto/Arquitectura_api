from fastapi import APIRouter, HTTPException, Depends
from auth.auth_bearer import JWTBearer
from auth.auth_handler import get_password_hash
from core.database import db
from models.users import User

router = APIRouter()

@router.post("/register")
async def register_user(user: User):
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user.password = get_password_hash(user.password)
    result = await db.users.insert_one(user.dict(by_alias=True))
    return {"id": str(result.inserted_id), "message": "User registered successfully"}
