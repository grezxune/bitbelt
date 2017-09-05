from mongoengine import *

class DefaultValues(Document):
    left_stile_width = FloatField(default=0.0)
    right_stile_width = FloatField(default=0.0)
    top_rail_width = FloatField(default=0.0)
    bottom_rail_width =  FloatField(default=0.0)
    left_overlay = FloatField(default=0.0)
    right_overlay = FloatField(default=0.0)
    top_overlay = FloatField(default=0.0)
    bottom_overlay = FloatField(default=0.0)
    panel_gap = FloatField(default=0.0)
    tennon_length = FloatField(default=0.0)
