from image import Image


class Item:
    """Item class"""

    # default constructor
    def __init__(self, name, price):
        self.upc = 0
        self.unit_price = price
        self.description = ""
        self.sample_picture = Image("path/to/file")
        self.item_name = name

    def getPrice(self):
        return self.unit_price




