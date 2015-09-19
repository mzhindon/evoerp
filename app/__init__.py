'''app PACKAGE CONSTRUCTOR
   INITIALIZE THE EXTENTIONS USED BY
   FLASK APP
'''

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
'''Import dictionary from config module
   dictionary config contains DevConfig and ProdConfig '''
from config import config

'''Because there is no application instance to 
   initialize the extentions, it creates them uninitialized
   passing no arguments into their constructors'''
bootstrap = Bootstrap()
db = SQLAlchemy()

'''APLICATION FACTORY FUNCTION'''
def create_app(config_name):
    app = Flask(__name__)
    '''Based on the name passed as argument to
       create_app method, it is used as key to
       get the config object asociated to tha key
       in this case can be DevConfig or ProdConfig classes'''
    app.config.from_object(config[config_name])
    '''Pass the object Flask referenced by the variable db
       to the Configuration Class obtained by key'''
    config[config_name].init_app(app)

    '''Once the application is created and configured
       the extentions can be initialized. Calling __init_app
       on the extentions that were created earlies completes
       their initialization'''
    bootstrap.init_app(app)
    db.init_app(app)

    '''Blueprints registre'''
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .inventory import inventory as inventory_blueprint
    app.register_blueprint(inventory_blueprint,url_prefix='/inventory')


    return app
