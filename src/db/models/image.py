# External
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Internal
from src.db.db import Base

# Code
class ImageDBM(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    url = Column(String)

    property_id = Column(Integer, ForeignKey('properties.id'))

    property = relationship('PropertyDBM', back_populates='images')