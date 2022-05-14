import os
class Config:
   QUOTES_API_URL='http://quotes.stormconsultancy.co.uk/random.json'
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:oderoh@localhost/jkblog'

class ProdConfig(Config):
    pass 



class DevConfig(Config):
    
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig  
} 