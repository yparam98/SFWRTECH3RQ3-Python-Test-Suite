from customer import Customer
from itemlist import ItemList


class Order:
    """Order class"""

    # default constructor
    def __init__(self):
        self.order_number = 0
        self.customer = Customer()
        self.price_paid = 0.0
        self.status = ""
        self.list = ItemList()
        self.date = ""
