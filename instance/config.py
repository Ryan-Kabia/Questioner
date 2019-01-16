"""
Enviroment Configurtions
"""

import os

class Config(object):
    """common configurations"""
    
    DEBUG = False
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
    """Development configurations"""
    DEBUG = True
    
class ProductionConfig(Config):

    """Production configurations"""
    
    DEBUG = False

class TestingConfig(Config):

    """Testing configurations"""
    TESTING = True
    DEBUG = True
    
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
       
