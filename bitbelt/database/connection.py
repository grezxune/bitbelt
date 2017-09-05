from mongoengine import *

class Connection(object):

    def __init__(self, app_config):
        connect(app_config['MONGO_DB_NAME'], host='localhost', port=27017)
