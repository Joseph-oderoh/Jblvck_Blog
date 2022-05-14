from . import main
from ..requests import get_quote
from ..models import Quotes
from flask import render_template,request


@main.route('/')
def index():
    """
     View root page function that returns the index page and its data
    """
    title = 'Welcome to the JBlvck_Blog home of the best Information in the net'
    
    quote=get_quote()
    return render_template('index.html', title=title, quote =quote)