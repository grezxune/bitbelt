from mongoengine import *
from bitbelt.models import *

class Door(Document):
    # Set by default values
    left_stile_width = FloatField(default=0.0)
    right_stile_width = FloatField(default=0.0)
    top_rail_width = FloatField(default=0.0)
    bottom_rail_width = FloatField(default=0.0)
    left_overlay = FloatField(default=0.0)
    right_overlay = FloatField(default=0.0)
    top_overlay = FloatField(default=0.0)
    bottom_overlay = FloatField(default=0.0)
    panel_gap = FloatField(default=0.0)
    tennon_length = FloatField(default=0.0)

    # Custom per door
    panels = ListField(ReferenceField('panel.Panel'))
    center_rails = ListField(ReferenceField('centerRail.CenterRail'))

    def __init__(self, default_values, panels, center_rails):
        self.left_stile_width = default_values['left_style_width']
        self.right_stile_width = default_values['right_style_width']
        self.top_rail_width = default_values['top_rail_width']
        self.bottom_rail_width = default_values['bottom_rail_width']
        self.left_overlay = default_values['left_overlay']
        self.right_overlay = default_values['right_overlay']
        self.top_overlay = default_values['top_overlay']
        self.bottom_overlay = default_values['bottom_overlay']
        self.panel_gap = default_values['panel_gap']
        self.tennon_length = default_values['tennon_length']

        self.panels = panels
        self.center_rails = center_rails