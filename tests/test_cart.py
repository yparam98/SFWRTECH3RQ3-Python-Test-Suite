from cart import Cart
from itemlist import ItemList
from listing import Listing
from jersey import Jersey


# itemlist -> listing -> item

def test_cart_subtotal_calculation():
    cart = Cart()

    cart.add_to_cart(Listing(Jersey("Raptors KyleLowry Jersey", 39.99), 2))
    cart.add_to_cart(Listing(Jersey("Celtics JaysenTatum Jersey", 29.99), 1))
    cart.add_to_cart(Listing(Jersey("Lakers LeBronJames Jersey", 59.99), 7))
    cart.add_to_cart(Listing(Jersey("Nuggets JamalMurray Jersey", 49.99), 5))

    assert (cart.get_subtotal_cost() == (39.99 + 29.99 + 59.99 + 49.99)), "cart subtotal does not match entered items!"


def test_cart_tax_calculation():
    cart = Cart()

    cart.add_to_cart(Listing(Jersey("Clippers KawhiLeonard Jersey", 39.99), 2))
    cart.add_to_cart(Listing(Jersey("Heats JimmyButler Jersey", 29.99), 1))
    cart.add_to_cart(Listing(Jersey("Bucks GiannisAntetokounmpo Jersey", 59.99), 7))
    cart.add_to_cart(Listing(Jersey("Rockets JamesHarden Jersey", 49.99), 5))

    assert (cart.get_tax_cost() == (
            ((39.99 + 29.99 + 59.99 + 49.99) / 100) * 13)
            ), "cart tax calculation does not match entered items!"


def test_cart_total_calculation():
    cart = Cart()

    cart.add_to_cart(Listing(Jersey("Warriors StephCurry Jersey", 39.99), 2))
    cart.add_to_cart(Listing(Jersey("Nets KyrieIrving Jersey", 29.99), 1))
    cart.add_to_cart(Listing(Jersey("Knicks DennisSmithJr Jersey", 59.99), 7))
    cart.add_to_cart(Listing(Jersey("Spurs DeMarDeRozan Jersey", 49.99), 5))

    subtotal = (39.99 + 29.99 + 59.99 + 49.99)
    tax = (((39.99 + 29.99 + 59.99 + 49.99) / 100) * 13)

    assert cart.get_total_cost() == (subtotal + tax), "cart subtotal does not match entered items!"


def test_cart_deletion():
    cart = Cart()

    # adding items to cart for test data
    cart.add_to_cart(Listing(Jersey("Warriors StephCurry Jersey", 39.99), 2))
    cart.add_to_cart(Listing(Jersey("Nets KyrieIrving Jersey", 29.99), 1))
    cart.add_to_cart(Listing(Jersey("Knicks DennisSmithJr Jersey", 59.99), 7))
    cart.add_to_cart(Listing(Jersey("Spurs DeMarDeRozan Jersey", 49.99), 5))

    # pass item to be deleted to the function
    assert cart.delete_from_cart(
        Listing(Jersey("Spurs DeMarDeRozan Jersey", 49.99), 5)), "match not found, cannot delete!"
