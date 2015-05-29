from flask import Blueprint

'''main Blueprint creation.
   This Blueprint has to be 
   registeres inside create_app() 
   factory function'''

main = Blueprint('main',__name__)

'''Importing views causes that routes inside
   this module to be asociated  with the blueprint'''
from . import views
