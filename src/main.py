# Internal
from src.utils import config
from src.db import db

from src.db.models.city import CityDBM
# from src.db.models.province import ProvinceDBM
from src.db.models.currency import CurrencyDBM
# from src.db.models.commodity import CommodityDBM
# from src.db.models.image import ImageDBM
# from src.db.models.property_type import PropertyTypeDBM
# from src.db.models.property import PropertyDBM


db.create_portfolio_db_and_tables()

def example_config():
    from sqlalchemy.orm import Session
    from src.db.db import engine
    from src.db.client import DataBaseClient
        
    session = Session(engine)
    db_client = DataBaseClient(session=session)
    
    new_city = CityDBM(name="Quilmes", province_id=1)
    db_client.save(new_city)
    
    # new_province = ProvinceDBM(name="Buenos Aires")
    # db_client.save(new_province)    

    currency = CurrencyDBM(name="USD")
    db_client.save(currency)    
    
# example_config()