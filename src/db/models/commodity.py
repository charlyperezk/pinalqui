# External
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Integer, Boolean
from sqlalchemy.orm import relationship

# Internal
from src.db.db import Base

# Code
class CommodityDBM(Base):
    __tablename__ = 'commodities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    capacity = Column(Integer)
    surface = Column(Float) 
    floors = Column(Integer) 
    rooms = Column(Integer)
    bedroom = (Integer) 
    bathroom = (Integer)
    parking = (Boolean) 
    elevator = (Boolean) 
    air_conditioning = (Boolean)
    
    property_id = Column(Integer, ForeignKey('properties.id'))

    property = relationship('PropertyDBM', back_populates='commodities')