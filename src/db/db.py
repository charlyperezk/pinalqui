# External
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Internal
from src.utils.config import Config
from src.utils.exceptions import DBEngineInitializationError

# Code
try:
    # engine = create_engine(os.getenv("DATABASE_URL"))
    DB_URL = Config.get_default_config('database_url')
    engine = create_engine(DB_URL)
except:
    raise DBEngineInitializationError("Failed creating engine")

Base = declarative_base()

def create_portfolio_db_and_tables():
    Base.metadata.create_all(bind=engine)