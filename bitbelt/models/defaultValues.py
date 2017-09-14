from mongoengine import *

class DefaultValues(Document):
    left_stile_width = DecimalField(default=0.0)
    right_stile_width = DecimalField(default=0.0)
    top_rail_width = DecimalField(default=0.0)
    bottom_rail_width =  DecimalField(default=0.0)
    left_overlay = DecimalField(default=0.0)
    right_overlay = DecimalField(default=0.0)
    top_overlay = DecimalField(default=0.0)
    bottom_overlay = DecimalField(default=0.0)
    panel_gap = DecimalField(default=0.0)
    tennon_length = DecimalField(default=0.0)
