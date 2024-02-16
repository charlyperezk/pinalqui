# External
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Internal
from src.db.db import Base

# Code
class ProvinceDBM(Base):
    __tablename__ = 'provinces'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    
    cities = relationship('CityDBM', back_populates='province')