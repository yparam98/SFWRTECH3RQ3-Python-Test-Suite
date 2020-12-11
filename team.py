from colourscheme import ColourScheme
from logo import Logo


class Team:
    """Team class"""
    logo: Logo

    # default constructor
    def __init__(self, name):
        self.team_name = name
        self.colour_scheme = ColourScheme("white","black")

    def set_colours(self, colour_scheme):
        self.colour_scheme = colour_scheme




