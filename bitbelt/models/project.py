import datetime
from mongoengine import Document, ReferenceField, ListField, DateTimeField, StringField, CASCADE

from bitbelt.models.default_values import DefaultValues
from bitbelt.models.client import Client
from bitbelt.models.cabinet_opening import CabinetOpening

class Project(Document):
    name = StringField(required=True)
    client = ReferenceField('Client', reverse_delete_rule=CASCADE, required=True)
    default_values = ReferenceField('DefaultValues', reverse_delete_rule=CASCADE, required=True)
    cabinet_openings = ListField(ReferenceField('CabinetOpening', reverse_delete_rule=CASCADE))
    wood_species = StringField(required=False)
    created_on = DateTimeField(required=True)


    def clean(self):
        print(self.created_on)
        if(self.created_on is None):
            self.created_on = datetime.datetime.now()

    
    def jsonify(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'client': self.client.jsonify(),
            'defaultValues': self.default_values.jsonify(),
            'cabinetOpenings': [cabinet_opening.jsonify() for cabinet_opening in self.cabinet_openings],
            'woodSpecies': self.wood_species,
            'createdOn': self.created_on
        }