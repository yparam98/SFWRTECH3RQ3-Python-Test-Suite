from item import Item
from customization import Customization


class Jersey(Item):
    """Jersey class"""

    # default constructor
    def __init__(self, name, unit_price):
        self.sku = 0
        self.modifications = Customization()
        self.size = ''
        self.is_modified = False
        Item.__init__(self, name, unit_price)

    def add_customizations(self, customizations):
        self.modifications = customizations
        self.is_modified = True
