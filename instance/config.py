class Config(object):
    """common configurations"""
    
    #put any configurations common across enviroments
    
class DevelopmentConfig(Config):
    """Development configurations"""
    DEBUG = True
    
class ProductionConfig(Config):

    """Production configurations"""
    
    DEBUG = False
    
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
       