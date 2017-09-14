from mongoengine import Document, ObjectIdField, StringField, EmailField
from bson.objectid import ObjectId

class User(Document):
    user_id = ObjectIdField(primary_key=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True)

    is_authenticated = True
    is_active = True
    is_anonymous = True


    def get_id(self):
        return str(self.user_id)


    def clean(self):
        if(self.user_id is None):
            print('setting user_id')
            self.user_id = ObjectId()