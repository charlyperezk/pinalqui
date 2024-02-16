# External
from sqlalchemy import Column, Integer, String

# Internal
from src.db.db import Base

# Code
class PropertyTypeDBM(Base):
    __tablename__ = 'property_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)