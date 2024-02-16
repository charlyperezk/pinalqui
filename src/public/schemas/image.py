# External
from pydantic import BaseModel
from typing import Type

# Code
class ImageCreate(BaseModel):
    title: Type[str]
    url: Type[str]

class ImageRead(ImageCreate):
    id: Type[int]
    