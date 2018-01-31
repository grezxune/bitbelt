from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
# from wtforms.validators import *
from wtforms.validators import required, Email, length
import bitbelt.forms

class SignUpForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[required()])
    last_name = StringField(label='Last Name', validators=[required()])
    email = StringField(label='Email Address', validators=[required(), Email()])
    password = PasswordField(label='Password', validators=[required(), length(min=5, max=15)])