# External
from pydantic import BaseModel
from typing import Type

# Code
class CommodityCreate(BaseModel):
    property_id: Type[int]
    name: Type[str]
    capacity: Type[int]
    surface: Type[float]
    floors: Type[int]
    rooms: Type[int]
    bedroom: Type[int]
    bathroom: Type[int]
    parking: Type[bool]
    elevator: Type[bool]
    air_conditioning: Type[bool]

class CommodityRead(CommodityCreate):
    id: Type[int]