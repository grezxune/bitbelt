from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import required, Email, length

class UserSettingsForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[required()])
    last_name = StringField(label='Last Name', validators=[required()])
    email = StringField(label='Email Address', validators=[required(), Email()])
    rough_sawn_overestimate = FloatField(label='Rough Sawn Overestimate')
