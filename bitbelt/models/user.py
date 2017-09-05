from mongoengine import *
from bson.objectid import ObjectId

class User(Document):
    user_id = StringField(primary_key=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    middle_name = StringField(required=False, default=None)
    email = EmailField(required=True)
    password = StringField(required=True)

    is_authenticated = True
    is_active = True
    is_anonymous = True


    def get_id(self):
        return self.user_id


    def clean(self):
        self.user_id = str(ObjectId())


    def __init__(self, first_name, last_name, middle_name, email, password, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.email = email
        self.password = password

    
