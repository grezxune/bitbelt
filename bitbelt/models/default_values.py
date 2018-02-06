from mongoengine import Document, FloatField, IntField
import time


class DefaultValues(Document):
    date_created = IntField(required=True)
    last_modified = IntField(required=True)

    left_stile_width = FloatField(default=0.0, precision=5)
    right_stile_width = FloatField(default=0.0, precision=5)
    top_rail_width = FloatField(default=0.0, precision=5)
    bottom_rail_width =  FloatField(default=0.0, precision=5)
    left_overlay = FloatField(default=0.0, precision=5)
    right_overlay = FloatField(default=0.0, precision=5)
    top_overlay = FloatField(default=0.0, precision=5)
    bottom_overlay = FloatField(default=0.0, precision=5)
    panel_gap = FloatField(default=0.0, precision=5)
    middle_gap = FloatField(default=0.0, precision=5)
    tennon_length = FloatField(default=0.0, precision=5)
    center_rail_width = FloatField(default=0.0, precision=5)


    def clean(self):
        currentTime = int(round(time.time() * 1000))
        if(self.date_created is None):
            self.date_created = currentTime
        self.last_modified = currentTime


    def jsonify(self):
        return {
            'dateCreated': self.date_created,
            'lastModified': self.last_modified,

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
            'centerRailWidth': self.center_rail_width
        }
