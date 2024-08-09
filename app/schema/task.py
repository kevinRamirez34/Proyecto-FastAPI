from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    id: Optional[int]= None
    title:str = Field(min_length=5,max_length=15)
    description:str = Field(min_length=5,max_length=50)
    to_do:bool = Field
    user_id: Optional[int]= None