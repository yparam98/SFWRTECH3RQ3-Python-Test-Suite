from displaytext import DisplayText


class Number(DisplayText):
    """Number class"""

    # default constructor
    def __init__(self):
        self.value = 0
        self.digit_count = 0
        DisplayText.__init__(self, "black")

    # verify number
    # see if number is within limitations
    def verify_number(self, number):
        self.value = number
        return None


