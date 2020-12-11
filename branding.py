from image import Image


class Branding(Image):
    """Branding class"""
    isTransparent: bool

    # default constructor
    def __init__(self, path):
        self.isTransparent = False
        Image.__init__(self, path)

    def is_transparent(self):
        return self.isTransparent


