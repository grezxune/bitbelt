from mongoengine import Document, ObjectIdField, StringField, EmailField
from passlib.hash import pbkdf2_sha256
from bson.objectid import ObjectId

class User(Document):
    user_id = ObjectIdField(primary_key=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True)


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
        if(self.user_id is None):
            print('setting user_id')
            self.user_id = ObjectId()
    

    def check_login(self, email, password):
        is_valid_login = False

        if(self.email == email and pbkdf2_sha256.verify(password, self.password)):
            is_valid_login = True

        return is_valid_login

    
    def hash_password(self, password):
        return pbkdf2_sha256.hash(password)
    


#  if form.validate_on_submit():
#             if User.query.filter_by(email=form.email.data).first():
#                 return "Email address already exists"
#             else:
#                 return "will create user here"