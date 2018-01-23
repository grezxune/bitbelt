from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, FloatField
# from wtforms.validators import *
import wtforms.validators
import bitbelt.forms
from bson import ObjectId

class CreateProject(FlaskForm):
    client = SelectField('Client', coerce=ObjectId)

    # Default Values
    left_stile_width = FloatField(label="Left Stile Width", default=0.0)
    right_stile_width = FloatField(label="Right Stile Width", default=0.0)
    top_rail_width = FloatField(label="Top Rail Width", default=0.0)
    bottom_rail_width =  FloatField(label="Bottom Rail Width", default=0.0)
    left_overlay = FloatField(label="Left Overlay", default=0.0)
    right_overlay = FloatField(label="Right Overlay", default=0.0)
    top_overlay = FloatField(label="Top Overlay", default=0.0)
    bottom_overlay = FloatField(label="Bottom Overlay", default=0.0)
    panel_gap = FloatField(label="Panel Gap", default=0.0)
    tennon_length = FloatField(label="Tennon Length", default=0.0)