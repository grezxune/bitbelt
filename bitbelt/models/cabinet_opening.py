from mongoengine import Document, FloatField, ReferenceField, IntField, BooleanField, CASCADE, StringField
import time

class CabinetOpening(Document):
    date_created = IntField(required=True)
    last_modified = IntField(required=True)

    # Custom per door
    number_of_openings = IntField(default=1)
    number_of_doors = IntField(default=1)
    number_of_panels_per_door = IntField(default=1)
    opening_width = FloatField(default=0.0, precision=5)
    opening_height = FloatField(default=0.0, precision=5)
    center_rail_horizontal = BooleanField(default=True)
    comments = StringField()

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
    middle_gap = FloatField(default=0.0, precision=5)
    tennon_length = FloatField(default=0.0, precision=5)
    center_rail_width = FloatField(default=0.0, precision=5)
    rough_sawn_overestimate = FloatField(default=0.0, precision=5)

    meta = {
        'ordering': ['-last_modified']
    }


    def clean(self):
        currentTime = int(round(time.time() * 1000))
        if(self.date_created is None):
            self.date_created = currentTime
        self.last_modified = currentTime

    
    def jsonify(self):
        return {
            'dateCreated': self.date_created,
            'lastModified': self.last_modified,

            'id': str(self.id),
            'numberOfOpenings': self.number_of_openings,
            'numberOfDoors': self.number_of_doors,
            'numberOfPanelsPerDoor': self.number_of_panels_per_door,
            'openingWidth': self.opening_width,
            'openingHeight': self.opening_height,
            'comments': self.comments,

            'leftStileWidth': self.left_stile_width,
            'rightStileWidth': self.right_stile_width,
            'topRailWidth': self.top_rail_width,
            'bottomRailWidth': self.bottom_rail_width,
            'leftOverlay': self.left_overlay,
            'rightOverlay': self.right_overlay,
            'topOverlay': self.top_overlay,
            'bottomOverlay': self.bottom_overlay,
            'panelGap': self.panel_gap,
            'middleGap': self.middle_gap,
            'tennonLength': self.tennon_length,
            'centerRailWidth': self.center_rail_width,
            'centerRailHorizontal': self.center_rail_horizontal,
            'roughSawnOverestimate': self.rough_sawn_overestimate,
        }



# At bottom of create opening, have button "Add Center Rails"
# Pop up window, allow user to create a list of items containing
#   1. Width (float)
#   2. Location (float) (If DefaultLocation selected, this is not editable)
#   3. DefaultLocation (bool)

# Popup returns list of GUIDs for these new center rails which were created
# Set reference field list of center rails on opening to these GUIDs
# Display number of center rails, and if they were defaulted or not