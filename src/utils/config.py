# External
import os
from dotenv import load_dotenv
load_dotenv()
import logging  

# Code
class Config:
    
    # This class is used to manage the configuration of the application. It will be imported by other modules and classes.
    
    default_value_declaration = {
            'properties': "PROPERTY_STATUS_ACTIVE",
            'database_url': "DATABASE_URL",
            'secret': "SECRET_KEY"
        }

    def __init__(self, check_start: bool=False):
        if check_start:
            self.app_starting_check()
            logging.info("Configurations checked")
        
    @classmethod
    def app_starting_check(cls):
        
        # This method  is used to check if the necessary environment variables are set. 
        # If not, it will log a warning and exit the application.
                
        default_config_lenght = len(cls.default_value_declaration)
        loaded = 0

        for key in cls.default_value_declaration.keys():
            try:
                cls.get_value_from_environment(cls.default_value_declaration[key])
                loaded+=1
            except Exception as e:
                logging.exception("%s",e)
                
        return False if not loaded == default_config_lenght else True
                
                
    @classmethod
    def get_value_from_environment(cls, key: str):
        try:
            config = os.getenv(key)
        except KeyError:
            raise ValueError('Key {} does not exist in Environment Variables'.format(key))
        except Exception as e:
            raise ValueError('Invalid value for key {}: {}'.format(key, e))
        if not config: 
            raise ValueError('Environment variable {} is empty'.format(key))
        else:
            return config
    
    
    @classmethod
    def get_default_config(cls, key):
        if isinstance(key, str) and key in cls.default_value_declaration:
            try:
                return cls.get_value_from_environment(key)
            except ValueError as e:
                logging.exception("%s",e)
                
                
config = Config(check_start=True)