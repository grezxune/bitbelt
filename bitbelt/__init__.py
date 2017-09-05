from flask import Flask
from bitbelt.settings import *
from bitbelt.database.connection import Connection
from flask_login import LoginManager
import os

app = Flask(import_name=__name__,
            template_folder='./templates',
            static_folder='./static')

app.secret_key = 'supa secrete keey'

if('MONGODB_URI' in os.environ is not None):
    app.config.from_object('bitbelt.settings.Production')
else:
    app.config.from_object('bitbelt.settings.Development')

login_manager = LoginManager()
login_manager.init_app(app)

mongo_connection = Connection(app.config)

import bitbelt.routes

if __name__ == '__main__':
    print('in main')
    app.run(host='localhost', port=2550)