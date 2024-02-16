# External
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Internal
from src.db.db import Base
from src.db.models.province import ProvinceDBM

# Code
class CityDBM(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    province_id = Column(Integer, ForeignKey('provinces.id'))

    province = relationship('ProvinceDBM', back_populates='cities')