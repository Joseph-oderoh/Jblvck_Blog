from datetime import datetime
from . import db
from flask_login import  UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin ,db.Model):
    __tablename__='user'
    id= db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String , unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    blogs = db.relationship('Blogs', backref='author', lazy = 'dynamic')
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    
class Blogs(db.Model):  
    __tablename__='blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String())
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    comments = db.relationship('comment',backref='blog' ,lazy='dynamic' )
    
    def save_blogs(self):
        db.session.add(self)
        db.session.commit()
    def repr(self):
        return f'Post {self.title}'
    
    
class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    date_posted= db.Column(db.DateTime,default=datetime.utcnow)
    blog_id= db.Column(db.ForeignKey("blog.id")) 
    user_id= db.Column(db.ForeignKey("user.id")) 
    
    def save_c(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return f'Comment {self.name}'
    
    
    
    
    
    
    
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
       