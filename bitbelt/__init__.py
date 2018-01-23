import os
from flask import Flask
from flask_login import LoginManager

from bitbelt.settings import Development, Production
from bitbelt.database.connection import Connection

app = Flask(import_name=__name__,
            template_folder='./templates',
            static_folder='./static')

if('MONGODB_URI' in os.environ is not None):
    app.config.from_object('bitbelt.settings.Production')
else:
    app.config.from_object('bitbelt.settings.Development')

# Make sure to set env variable SECRET_KEY on heroku
app.secret_key = os.environ.get('SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)

mongo_connection = Connection(app.config)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
import bitbelt.routes

if __name__ == '__main__':
    port = 2550
    print('[+] Running BitBelt on localhost:{0}'.format(port))
    app.run(host='localhost', port=port)
