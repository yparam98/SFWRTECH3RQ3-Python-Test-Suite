from image import Image


class Logo(Image):
    """Logo class"""

    # default constructor
    def __init__(self, path):
        self.name = ""
        Image.__init__(path)
