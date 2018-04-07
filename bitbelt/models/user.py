from mongoengine import Document, ObjectIdField, StringField, EmailField, ReferenceField, ListField, DENY, PULL, IntField
from passlib.hash import pbkdf2_sha256
from bson.objectid import ObjectId
import time

from bitbelt.models.user_settings import UserSettings
from bitbelt.models.project import Project
from bitbelt.models.client import Client

class User(Document):
    date_created = IntField(required=True)
    last_modified = IntField(required=True)

    user_id = ObjectIdField(primary_key=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    settings = ReferenceField('UserSettings', reverse_delete_rule=DENY, required=True)
    projects = ListField(ReferenceField('Project', reverse_delete_rule=PULL, required=False))
    clients = ListField(ReferenceField('Client', reverse_delete_rule=PULL, required=False))


    @property
    def is_authenticated(self):
        return True


    @property
    def is_active(self):
        return True


    @property
    def is_anonymous(self):
        return False


    def get_id(self):
        return str(self.user_id)


    def clean(self):
        currentTime = int(round(time.time() * 1000))

        if(self.user_id is None):
            self.user_id = ObjectId()

        if(self.date_created is None):
            self.date_created = currentTime

        self.last_modified = currentTime
    

    def check_login(self, email, password):
        is_valid_login = False

        if(self.email == email and pbkdf2_sha256.verify(password, self.password)):
            is_valid_login = True

        return is_valid_login

    
    def hash_password(self, password):
        return pbkdf2_sha256.hash(password)


    def jsonify(self):
        return {
            'dateCreated': self.date_created,
            'lastModified': self.last_modified,
            'id': str(self.user_id),
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'settings': self.settings.jsonify(),
            'projects': self.projects.jsonify(),
            'clients': self.clients.jsonify()
        }


#  if form.validate_on_submit():
#             if User.query.filter_by(email=form.email.data).first():
#                 return "Email address already exists"
#             else:
#                 return "will create user here"