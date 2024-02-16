# External
from pydantic import BaseModel
from typing import Type

# Code
class CityCreate(BaseModel):
    name: Type[str]
    province_id: Type[int]
    
class CityRead(CityCreate):
    id: Type[int]