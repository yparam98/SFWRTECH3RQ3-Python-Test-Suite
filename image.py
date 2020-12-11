class Image:
    """Image class"""

    # default constructor
    def __init__(self, path):
        self.image_path = path
        self.height = 0.0
        self.width = 0.0
        self.type = None

    def getType(self):
        return self.type
