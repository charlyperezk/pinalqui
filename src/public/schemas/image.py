# External
from pydantic import BaseModel
from typing import Type

# Code
class ImageRead(BaseModel):
    id: Type[int]
    title: Type[str]
    url: Type[str]