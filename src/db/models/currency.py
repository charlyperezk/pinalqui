# External
from sqlalchemy import Column, Integer, String

# Internal
from src.db.db import Base

# Code
class CurrencyDBM(Base):
    __tablename__ = 'currencies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)