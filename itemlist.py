from listing import Listing
from item import Item


class ItemList:
    """ItemList class"""

    # default constructor
    def __init__(self):
        self.listings = []
        self.is_modified = False

    def add(self, listing):
        self.listings.append(listing)

