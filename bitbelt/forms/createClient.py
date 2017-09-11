from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FieldList
# from wtforms.validators import *
from wtforms.validators import required, length, Email
import bitbelt.forms

class CreateClient(FlaskForm):
    first_name = StringField(label='First Name', validators=[required()])
    last_name = StringField(label='Last Name', validators=[required()])
    address = StringField(label='Address', validators=[required()])
    city = StringField(label='City', validators=[required()])
    state = StringField(label='State', validators=[required()])
    zip_code = StringField(label='Zip Code', validators=[required()])
    # phone = FieldList(StringField(label='Phones'))
    email = StringField(label='Email Address', validators=[required(), Email()])