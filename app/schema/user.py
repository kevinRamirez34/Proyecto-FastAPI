from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[int]= None
    username: str = Field(min_length=5,max_length=15)
    email: str = Field(min_length=5,max_length=50)