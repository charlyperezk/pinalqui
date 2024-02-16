# External
from pydantic import BaseModel
from typing import Type, List

# Internal
from src.public.schemas.city import CityRead

# Code
class ProvinceCreate(BaseModel):
    name: Type[str]
    
class ProvinceRead(ProvinceCreate):
    cities: List[CityRead]