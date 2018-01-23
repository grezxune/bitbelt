from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import required, Email, length

class Login(FlaskForm):
    email = StringField(label='Email Address', validators=[required(), Email()])
    password = PasswordField(label='Password', validators=[required(), length(min=5, max=15)])