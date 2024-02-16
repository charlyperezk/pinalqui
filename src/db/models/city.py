# External
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Internal
from db.db import Base

# Code
class CityDBM(Base):
    __tablename__ = 'provinces'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    province_id = Column(Integer, ForeignKey('provincies.id'))

    province = relationship('ProvinceDBM', back_populates='cities')