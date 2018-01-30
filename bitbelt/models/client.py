from mongoengine import StringField, ListField, EmailField, Document, ReferenceField, CASCADE
from bitbelt.models import user

class Client(Document):
    user_id = ReferenceField('user.User', required=True, reverse_delete_rule=CASCADE)

    first_name = StringField(required=True)
    last_name = StringField(required=True)
    address = StringField(required=True)
    city = StringField(required=True)
    state = StringField(required=True)
    zip_code = StringField(required=True)
    phone = ListField(StringField())
    email = EmailField(required=True)


    def jsonify(self):
        return {
            'userID': str(self.user_id.id),
            'firstName': self.first_name,
            'lastName': self.last_name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zipCode': self.zip_code,
            'phone': self.phone,
            'email': self.email
        }
