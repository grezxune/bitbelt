import datetime
import time
from mongoengine import Document, ReferenceField, ListField, DateTimeField, StringField, CASCADE, IntField, BooleanField

from bitbelt.models.default_values import DefaultValues
from bitbelt.models.client import Client
from bitbelt.models.cabinet_opening import CabinetOpening

class Project(Document):
    date_created = IntField(required=True)
    last_modified = IntField(required=True)

    name = StringField(required=True)
    client = ReferenceField('Client', reverse_delete_rule=CASCADE, required=True)
    default_values = ReferenceField('DefaultValues', reverse_delete_rule=CASCADE, required=True)
    cabinet_openings = ListField(ReferenceField('CabinetOpening', reverse_delete_rule=CASCADE))
    wood_species = StringField(required=False)
    is_finished = BooleanField(required=True)

    meta = {
        'ordering': ['-last_modified']
    }


    def clean(self):
        currentTime = int(round(time.time() * 1000))

        if(self.date_created is None):
            self.date_created = currentTime
            self.is_finished = False

        self.last_modified = currentTime


    def jsonify(self):
        return {
            'dateCreated': self.date_created,
            'lastModified': self.last_modified,
            'id': str(self.id),
            'name': self.name,
            'client': self.client.jsonify(),
            'defaultValues': self.default_values.jsonify(),
            'cabinetOpenings': [cabinet_opening.jsonify() for cabinet_opening in self.cabinet_openings],
            'woodSpecies': self.wood_species,
            'isFinished': self.is_finished
        }
