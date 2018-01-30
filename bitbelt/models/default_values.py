from mongoengine import Document, FloatField

class DefaultValues(Document):
    left_stile_width = FloatField(default=0.0, precision=5)
    right_stile_width = FloatField(default=0.0, precision=5)
    top_rail_width = FloatField(default=0.0, precision=5)
    bottom_rail_width =  FloatField(default=0.0, precision=5)
    left_overlay = FloatField(default=0.0, precision=5)
    right_overlay = FloatField(default=0.0, precision=5)
    top_overlay = FloatField(default=0.0, precision=5)
    bottom_overlay = FloatField(default=0.0, precision=5)
    panel_gap = FloatField(default=0.0, precision=5)
    tennon_length = FloatField(default=0.0, precision=5)


    def jsonify(self):
        return {
            'leftStileWidth': self.left_stile_width,
            'rightStileWidth': self.right_stile_width,
            'topRailWidth': self.top_rail_width,
            'bottomRailWidth': self.bottom_rail_width,
            'leftOverlay': self.left_overlay,
            'rightOverlay': self.right_overlay,
            'topOverlay': self.top_overlay,
            'bottomOverlay': self.bottom_overlay,
            'panelGap': self.panel_gap,
            'tennonLength': self.tennon_length
        }