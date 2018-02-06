from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, FloatField, StringField
from wtforms.validators import required
import bitbelt.forms
from bson import ObjectId

class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[required()])
    client = SelectField('Client', coerce=ObjectId)
    wood_species = StringField('Wood Species')

    # Default Values
    left_stile_width = FloatField(label="Left Stile Width")
    right_stile_width = FloatField(label="Right Stile Width")
    top_rail_width = FloatField(label="Top Rail Width")
    bottom_rail_width =  FloatField(label="Bottom Rail Width")
    left_overlay = FloatField(label="Left Overlay")
    right_overlay = FloatField(label="Right Overlay")
    top_overlay = FloatField(label="Top Overlay")
    bottom_overlay = FloatField(label="Bottom Overlay")
    panel_gap = FloatField(label="Panel Gap")
    middle_gap = FloatField(label="Middle Gap")
    tennon_length = FloatField(label="Tennon Length")
    center_rail_width = FloatField(label="Center Rail Width")