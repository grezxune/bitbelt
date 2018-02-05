from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FieldList
from wtforms.validators import required, length, Email
import bitbelt.forms

class AddClientForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[required()])
    last_name = StringField(label='Last Name', validators=[required()])
    address = StringField(label='Address')
    city = StringField(label='City')
    state = StringField(label='State')
    zip_code = StringField(label='Zip Code')
    phone = StringField(label='Phone')
    email = StringField(label='Email Address')