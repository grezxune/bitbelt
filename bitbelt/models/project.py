from mongoengine import *
from bitbelt.models.defaultValues import DefaultValues
# Fix how this import works, could be done like the default values one in this file
from bitbelt.models import client

class Project(Document):
    client = ReferenceField('client.Client', reverse_delete_rule=CASCADE)
    default_values = ReferenceField('DefaultValues', reverse_delete_rule=CASCADE)
    doors = ListField(ReferenceField('Door'))

    def __init__(self, client, default_values, *args, **kwargs):
        super(Document, self).__init__(default_values)
        self.client = client
        self.default_values = default_values
