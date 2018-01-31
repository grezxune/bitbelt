from flask_wtf import FlaskForm
from wtforms import SelectField, FloatField, IntegerField
# from wtforms.validators import *
import wtforms.validators
import bitbelt.forms
from bson import ObjectId

class CreateCabinetOpening(FlaskForm):
    # Default Values
    left_stile_width = FloatField(label="Left Stile Width", default=0.0)
    right_stile_width = FloatField(label="Right Stile Width", default=0.0)
    top_rail_width = FloatField(label="Top Rail Width", default=0.0)
    bottom_rail_width = FloatField(label="Bottom Rail Width", default=0.0)
    left_overlay = FloatField(label="Left Overlay", default=0.0)
    right_overlay = FloatField(label="Right Overlay", default=0.0)
    top_overlay = FloatField(label="Top Overlay", default=0.0)
    bottom_overlay = FloatField(label="Bottom Overlay", default=0.0)
    panel_gap = FloatField(label="Panel Gap", default=0.0)
    tennon_length = FloatField(label="Tennon Length", default=0.0)
    center_rail_width = FloatField(label="Center Rail Width", default=0.0)

    # Custom Values
    number_of_openings = IntegerField(label="Openings with these dimensions", default=1)
    number_of_doors = IntegerField(label="Doors per Opening", default=1)
    number_of_panels_per_door = IntegerField(label="Panels per Door", default=1)
    opening_width = FloatField(label="Opening Width", default=0.0)
    opening_height = FloatField(label="Opening Height", default=0.0)
    middle_gap = FloatField(label="Middle Gap", default=0.0)