# External
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# Internal
from db.db import Base
from utils.config import Config

# Code
DEFAULT_PROPERTY_STATUS = Config.get_default_config('properties')

class PropertyDBM(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime(timezone=True), default=func.now())
    title = Column(String)
    address = Column(String)
    price = Column(Float)
    deposit = Column(Float)
    description = Column(String)
    status = Column(String, default=DEFAULT_PROPERTY_STATUS)
    longitude = Column(String)
    latitude = Column(String)
    
    type_id = Column(Integer, ForeignKey('property_types.id'))
    city_id = Column(Integer, ForeignKey('cities.id'))
    commodities_id = Column(Integer, ForeignKey('property_commodities.id'))
    currency_id = Column(Integer, ForeignKey('currencies.id'))
    user_id = Column(Integer, ForeignKey('property_images.id'), default=None)
    
    images = relationship('ImageDBM', back_populates='properties')
    commodities = relationship('CommodityDBM', back_populates='properties')
    # user = relationship('UserDbModel')