from mongoengine import Document, FloatField

class CenterRail(Document):
    width = FloatField(default=0.0, precision=5)
    height = FloatField(default=0.0, precision=5)

    def __init__(self, width, height):
        self.width = width
        self.height = height

