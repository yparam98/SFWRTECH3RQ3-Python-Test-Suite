from image import Image


class ColourScheme:
    """ColourScheme class"""

    # default constructor
    def __init__(self, pri, sec):
        self.primary_colour = pri
        self.secondary_colour = sec
        self.template_img = Image("path/to/file")


