from mongoengine import Document, FloatField

class UserSettings(Document):
    rough_sawn_overestimate = FloatField(default=0.0, precision=5)


    def jsonify(self):
        return {
            'id': str(self.id),
            'roughSawnOverestimate': self.rough_sawn_overestimate
        }
