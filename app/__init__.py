from flask import Flask
from config import config_options

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    
    
    
    
    
    
    
  # setting config
    from .requests import configure_request
    configure_request(app)
  
  
    return app    