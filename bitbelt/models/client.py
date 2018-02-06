from mongoengine import StringField, ListField, EmailField, Document, ReferenceField, CASCADE, BooleanField, IntField
import time


class Client(Document):
    date_created = IntField(required=True)
    last_modified = IntField(required=True)

    first_name = StringField(required=True)
    last_name = StringField(required=True)
    address = StringField()
    city = StringField()
    state = StringField()
    zip_code = StringField()
    phone = StringField()
    email = EmailField()
    is_active = BooleanField(required=True)


    def clean(self):
        currentTime = int(round(time.time() * 1000))
        if(self.date_created is None):
            self.date_created = currentTime
            self.is_active = True
        self.last_modified = currentTime


    def jsonify(self):
        return {
            'dateCreated': self.date_created,
            'lastModified': self.last_modified,

            'firstName': self.first_name,
            'lastName': self.last_name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zipCode': self.zip_code,
            'phone': self.phone,
            'email': self.email,
            'isActive': self.is_active
        }
