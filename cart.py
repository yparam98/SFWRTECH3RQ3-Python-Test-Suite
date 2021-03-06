from itemlist import ItemList
from customer import Customer


class Cart:
    """Cart class"""

    # default constructor
    def __init__(self):
        self.item_list = ItemList()
        self.subtotal_cost = 0.00
        self.tax_cost = 0.00
        self.shipping_cost = 0.00
        self.total_cost = 0.00
        self.shopper = Customer()

    def add_to_cart(self, listing):
        self.item_list.add(listing)
        self.subtotal_cost += listing.total

    def delete_from_cart(self, listing):
        for entry in self.item_list.listings:
            if listing.item.item_name == entry.listing.item.item_name:
                self.item_list.listings.remove() # remove that element from list
        return None

    def get_total_cost(self):
        return self.total_cost

    def get_subtotal_cost(self):
        return self.subtotal_cost

    def get_tax_cost(self):
        return self.tax_cost




