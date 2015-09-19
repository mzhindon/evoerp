#!/usr/bin/env python
import os
from app import create_app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app.models.inventory import Category, Item
from app.models.vehicle import Vehicle
from app.models.common import Brand

'''Create the application using the APLICATION FACTORY FUNCTION create_app,
   we define wich aplication config use by setting a enviroment variable or
   if it does not exist we use a default configuration that correspond to 
   DevelopmentConfig in the dictionary'''

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app, db=db, Category = Category, Vehicle = Vehicle, Brand = Brand, Item = Item)

manager.add_command("shell", Shell(make_context=make_shell_context))
'''Flask exposes the database migration commands through a MigrateCommand
   that is attached to Flask-script manager'''
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
