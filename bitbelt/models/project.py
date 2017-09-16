import datetime

from mongoengine import Document, ReferenceField, ListField, DateTimeField, CASCADE
from bitbelt.models.defaultValues import DefaultValues
# Fix how this import works, could be done like the default values one in this file
from bitbelt.models import client, user, door

class Project(Document):
    user = ReferenceField('user.User', reverse_delete_rule=CASCADE, required=True)
    client = ReferenceField('client.Client', reverse_delete_rule=CASCADE, required=True)
    default_values = ReferenceField('DefaultValues', reverse_delete_rule=CASCADE, required=True)
    doors = ListField(ReferenceField('door.Door'))
    created_on = DateTimeField(required=True)


    def clean(self):
        print(self.created_on)
        if(self.created_on is None):
            self.created_on = datetime.datetime.now()