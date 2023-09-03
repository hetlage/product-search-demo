import os

from dotenv import load_dotenv

load_dotenv()

class Config():
    """
    Base configuration class. Contains default configuration settings + configuration settings applicable to all environments.
    """
    pass

class DevConfig(Config):
    MONGO_URL = os.environ.get('MONGO_URL') 

class TestConfig(Config):
    pass

class ProdConfig(Config):
    pass

config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
    'default': DevConfig
}