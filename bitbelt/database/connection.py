from mongoengine import *

class Connection(object):

    def __init__(self, app_config):
        connect(app_config['MONGO_DB_NAME'], host=app_config['MONGO_SERVER'], port=app_config['MONGO_PORT'])
