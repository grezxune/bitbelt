import os
from dotenv import load_dotenv

class Config(object):
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'tomtrezb2003@gmail.com'
    MAIL_PASSWORD = ''
    ADMIN_EMAILS = ['tomtrezb2003@gmail.com']

class Development(Config):
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env.dev')
    load_dotenv(dotenv_path)

    DEBUG = True
    MONGO_SERVER = 'localhost'
    MONGO_PORT = 27017
    MONGO_DB_NAME = 'BitBelt'
    MONGO_ALIAS = 'default'
    MONGODB_SETTINGS = { 'db': MONGO_DB_NAME, 'alias': MONGO_ALIAS }

class Production(Config):
    DEBUG = False
    MONGO_SERVER = os.environ['MONGODB_URI'] if 'MONGODB_URI' in os.environ else 'localhost'
    MONGO_PORT = 27017
    MONGO_DB_NAME = 'BitBelt'
    MONGO_ALIAS = 'default'
    MONGODB_SETTINGS = { 'db': MONGO_DB_NAME, 'alias': MONGO_ALIAS }