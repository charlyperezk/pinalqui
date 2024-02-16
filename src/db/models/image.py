# External
from sqlalchemy import Column, Integer, String, ForeignKey

# Internal
from db.db import Base
from utils.config import Config

# Code
class ImageDBM(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    url = Column(String)
    
    property_id = Column(Integer, ForeignKey('property.id'))