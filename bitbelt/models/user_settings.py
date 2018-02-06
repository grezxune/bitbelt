from mongoengine import Document, FloatField, IntField
import time


class UserSettings(Document):
    date_created = IntField(required=True)
    last_modified = IntField(required=True)

    rough_sawn_overestimate = FloatField(default=0.0, precision=5)


    def clean(self):
        currentTime = int(round(time.time() * 1000))
        if(self.date_created is None):
            self.date_created = currentTime
        self.last_modified = currentTime


    def jsonify(self):
        return {
            'dateCreated': self.date_created,
            'lastModified': self.last_modified,

            'id': str(self.id),
            'roughSawnOverestimate': self.rough_sawn_overestimate
        }
