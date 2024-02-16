# External
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Internal
from db.db import Base

# Code
class ProvinceDBM(Base):
    __tablename__ = 'provinces'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    
    cities = relationship('CityDBM', back_populates='provinces')