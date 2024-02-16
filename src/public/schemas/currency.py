# External
from pydantic import BaseModel
from typing import Type

# Code
class CurrencyCreate(BaseModel):
    name: Type[str]

class CurrencyRead(CurrencyCreate):
    id: Type[int]