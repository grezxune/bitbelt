class Panel(Document):
    width: FloatField(default=0.0)
    height: FloatField(default=0.0)

    def __init__(self, width, height):
        self.width = width
        self.height = height
