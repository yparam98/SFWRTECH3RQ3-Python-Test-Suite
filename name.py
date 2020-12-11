from displaytext import DisplayText


class Name(DisplayText):
    """Name class"""

    # default constructor
    def __init__(self):
        self.value = ""
        self.length = 0
        self.is_clean = False
        DisplayText.__init__(self, "black")

    # verify name
    # see if name is within size limitations
    def verify_name(self, name):
        self.value = name
        return None

    # returns true if name contains no profanities.
    # false otherwise...
    def isClean(self, name):
        self.value = name
        return None

    # user chose not to customize
    # set default options
    def setDefault(self):
        self.value = "Kyle Lowry"
        return None
