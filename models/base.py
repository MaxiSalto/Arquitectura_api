from pydantic import BaseModel, Field
from typing import Optional

class BaseModelWithId(BaseModel):
    id: Optional[str] = Field(alias="_id")
