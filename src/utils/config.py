# External
import os
from dotenv import load_dotenv
load_dotenv()
import logging

# Code
class Config:
    
    # This class is used to manage the configuration of the application. It will be imported by other modules and classes.
    
    default_value_declaration = {
            'properties': 'PROPERTY_STATUS_ACTIVE'
        }
    
    @classmethod
    def app_starting_check(cls):
        
        # This method  is used to check if the necessary environment variables are set. 
        # If not, it will log a warning and exit the application.
        
        default_config_lenght = len(cls.default_value_declaration)
        loaded = 0

        for key, value in cls.default_value_declaration:
            try:
                cls.get_value_from_environment(value)
                loaded+=1
            except ValueError:
                logging.error("Environment variable for %s is missing or invalid.", key)
            except Exception as e:
                logging.exception("%s",e)
                
        return False if not loaded == default_config_lenght else True
                
                
    @classmethod
    def get_value_from_environment(cls, key):
        config = os.getenv(cls.default_value_declaration[key])
        if not config: 
            raise ValueError('Environment variable {} is empty'.format(key))
        return config
    
    
    @classmethod
    def get_default_config(cls, key):
        if isinstance(key, str) and key in cls.default_value_declaration:
            try:
                return cls.get_value_from_environment(key)
            except ValueError:
                logging.error("Environment variable for %s is missing or invalid.", key)
            except Exception as e:
                logging.exception("%s",e)