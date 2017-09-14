from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField
# from wtforms.validators import *
import wtforms.validators
import bitbelt.forms
from bson import ObjectId

class CreateProject(FlaskForm):
    client = SelectField('Client', coerce=ObjectId)

    # Default Values
    left_stile_width = DecimalField(label="Left Stile Width", default=0.0)
    right_stile_width = DecimalField(label="Right Stile Width", default=0.0)
    top_rail_width = DecimalField(label="Top Rail Width", default=0.0)
    bottom_rail_width =  DecimalField(label="Bottom Rail Width", default=0.0)
    left_overlay = DecimalField(label="Left Overlay", default=0.0)
    right_overlay = DecimalField(label="Right Overlay", default=0.0)
    top_overlay = DecimalField(label="Top Overlay", default=0.0)
    bottom_overlay = DecimalField(label="Bottom Overlay", default=0.0)
    panel_gap = DecimalField(label="Panel Gap", default=0.0)
    tennon_length = DecimalField(label="Tennon Length", default=0.0)