# External
from pydantic import BaseModel
from typing import Type, List
from datetime import datetime
# Internal
from src.public.schemas.image import ImageRead

# Code
class PropertyCreate(BaseModel):
    date: Type[datetime]
    title: Type[str]
    address: Type[str]
    price: Type[float]
    deposit: Type[float]
    description: Type[str]
    status: Type[str]
    type_id: Type[int]
    city_id: Type[int]
    currency_id: Type[int]
    user: Type[int]
    
class PropertyRead(BaseModel):
    id: Type[int]
    date: Type[datetime]
    title: Type[str]
    address: Type[str]
    price: Type[float]
    deposit: Type[float]
    description: Type[str]
    status: Type[str]
    longitude: Type[str]
    latitude: Type[str]        
    # type: Type[PropertyTypeRead]
    # city: Type[CityRead]
    # commodities: Type[CommoditiesRead]
    # currency: Type[CurrencyRead]
    # user: Type[UserRead]
    images: List[ImageRead]