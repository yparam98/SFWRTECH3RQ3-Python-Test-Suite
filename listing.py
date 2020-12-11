from jersey import Jersey


class Listing:
    """Listing class"""

    # default constructor
    def __init__(self, in_item, in_quantity):
        self.item = in_item
        self.quantity = in_quantity
        self.total = self.item.unit_price * self.quantity
