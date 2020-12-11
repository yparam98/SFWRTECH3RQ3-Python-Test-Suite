from team import Team
from name import Name
from number import Number
from branding import Branding


class Customization:
    """Customization class"""

    # default constructor
    def __init__(self):
        self.team = Team("")
        self.name = Name()
        self.number = Number()
        self.branding = Branding("")

    def add_team(self, in_team):
        self.team = in_team

    def add_name(self, in_name):
        if self.name.verify_name(in_name):
            self.name.value = in_name
            return True
        else:
            return False

    def add_number(self, in_number):
        if self.number.verify_number(in_number):
            self.number.value = in_number
            return True
        else:
            return False

    def add_branding(self, in_branding):
        self.branding.image_path = in_branding
        return self.branding.getType() == "png" and self.branding.is_transparent()

    def verify_customizations(self):
        return self.branding.getType() == "png" \
               and self.branding.is_transparent() \
               and self.number.verify_number(self.number) \
               and self.name.verify_name(self.name)
