from mongoengine import *
from bitbelt.models.defaultValues import DefaultValues

class Project(Document):
    name = StringField(required=True, min_length=3, max_length=100)
    default_values = ReferenceField('DefaultValues', reverse_delete_rule=CASCADE)
    doors = ListField(ReferenceField('Door'))

    def __init__(self, name, default_values, *args, **kwargs):
        super(Document, self).__init__(default_values)
        self.default_values = default_values
