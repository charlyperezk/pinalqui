# External
from pydantic import BaseModel
from typing import Type

# Code
class PropertyTypeCreate(BaseModel):
    name: Type[str]
    
class PropertyTypeRead(PropertyTypeCreate):
    id: Type[int]