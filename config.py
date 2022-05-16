import os
class Config:
   UPLOADED_PHOTOS_DEST ='app/static/photos' 
   QUOTES_API_URL='http://quotes.stormconsultancy.co.uk/random.json'
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:oderoh@localhost/jkblog'
   SECRET_KEY = os.environ.get('SECRET_KEY')
   
# email configurations
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = False
   MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
   MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
class ProdConfig(Config):
   
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1) 
    
    
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX = 'upitch'
    DEBUG = True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:oderoh@localhost/jkblog'
    
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig  
} 