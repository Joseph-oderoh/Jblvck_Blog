from . import db
from flask_login import  UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin ,db.Model):
    __tablename__='users'
    id= db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String , unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
class Comment(db.Model):
    
    id = db.Column(db.models.Integer, primary_key=True)
    

class Quotes:
    """
     '''
    Quotes class to define Quotes Objects
    '''
    """
    def __init__(self,author,quote,url):
        
        self.author = author
        self.quote = quote
        self.url = url
       