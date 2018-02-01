from mongoengine import Document, FloatField, ReferenceField, IntField, BooleanField, CASCADE

class CabinetOpening(Document):
    # Custom per door
    number_of_openings = IntField(default=1)
    number_of_doors = IntField(default=1)
    number_of_panels_per_door = IntField(default=1)
    opening_width = FloatField(default=0.0, precision=5)
    opening_height = FloatField(default=0.0, precision=5)
    middle_gap = FloatField(default=0.0, precision=5)
    center_rail_horizontal = BooleanField(default=True)

    # A center rail should consist of a width, and location
    #center_rails = ListField(ReferenceField('centerRail.CenterRail'))

    # Set by default values
    left_stile_width = FloatField(default=0.0, precision=5)
    right_stile_width = FloatField(default=0.0, precision=5)
    top_rail_width = FloatField(default=0.0, precision=5)
    bottom_rail_width = FloatField(default=0.0, precision=5)
    left_overlay = FloatField(default=0.0, precision=5)
    right_overlay = FloatField(default=0.0, precision=5)
    top_overlay = FloatField(default=0.0, precision=5)
    bottom_overlay = FloatField(default=0.0, precision=5)
    panel_gap = FloatField(default=0.0, precision=5)
    tennon_length = FloatField(default=0.0, precision=5)
    center_rail_width = FloatField(default=0.0, precision=5)
    rough_sawn_overestimate = FloatField(default=0.0, precision=5)

    # def __init__(self, default_values, number_of_openings, number_of_doors, opening_width, opening_height, middle_gap):
    #     self.left_stile_width = default_values['left_style_width']
    #     self.right_stile_width = default_values['right_style_width']
    #     self.top_rail_width = default_values['top_rail_width']
    #     self.bottom_rail_width = default_values['bottom_rail_width']
    #     self.left_overlay = default_values['left_overlay']
    #     self.right_overlay = default_values['right_overlay']
    #     self.top_overlay = default_values['top_overlay']
    #     self.bottom_overlay = default_values['bottom_overlay']
    #     self.panel_gap = default_values['panel_gap']
    #     self.tennon_length = default_values['tennon_length']

    #     self.number_of_openings = number_of_openings
    #     self.number_of_doors = number_of_doors
    #     self.opening_width = opening_width
    #     self.opening_height = opening_height
    #     self.middle_gap = middle_gap

        #self.center_rails = center_rails

    
    def jsonify(self):
        return {
            'id': str(self.id),
            'numberOfOpenings': self.number_of_openings,
            'numberOfDoors': self.number_of_doors,
            'numberOfPanelsPerDoor': self.number_of_panels_per_door,
            'openingWidth': self.opening_width,
            'openingHeight': self.opening_height,
            'middleGap': self.middle_gap,

            'leftStileWidth': self.left_stile_width,
            'rightStileWidth': self.right_stile_width,
            'topRailWidth': self.top_rail_width,
            'bottomRailWidth': self.bottom_rail_width,
            'leftOverlay': self.left_overlay,
            'rightOverlay': self.right_overlay,
            'topOverlay': self.top_overlay,
            'bottomOverlay': self.bottom_overlay,
            'panelGap': self.panel_gap,
            'tennonLength': self.tennon_length,
            'centerRailWidth': self.center_rail_width,
            'centerRailHorizontal': self.center_rail_horizontal,
            'roughSawnOverestimate': self.rough_sawn_overestimate
        }



# At bottom of create opening, have button "Add Center Rails"
# Pop up window, allow user to create a list of items containing
#   1. Width (float)
#   2. Location (float) (If DefaultLocation selected, this is not editable)
#   3. DefaultLocation (bool)

# Popup returns list of GUIDs for these new center rails which were created
# Set reference field list of center rails on opening to these GUIDs
# Display number of center rails, and if they were defaulted or not