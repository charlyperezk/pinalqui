# External
from sqlalchemy import Column, Integer, String

# Internal
from db.db import Base

# Code
class CurrencyDBM(Base):
    __tablename__ = 'currencies'
    currency_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)