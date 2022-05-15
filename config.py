import os
class Config:
   UPLOADED_PHOTOS_DEST ='app/static/photos' 
   QUOTES_API_URL='http://quotes.stormconsultancy.co.uk/random.json'
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:oderoh@localhost/jkblog'
   SECRET_KEY = os.environ.get('SECRET_KEY')
class ProdConfig(Config):
    pass 



class DevConfig(Config):
    
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig  
} 