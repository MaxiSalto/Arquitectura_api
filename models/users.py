from models.base import BaseModelWithId
from typing import List, Optional

class User(BaseModelWithId):
    username: str
    email: str
    password: str
    role: str = "user"
    favorites: Optional[List[str]] = []
