"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for item in set(items_to_add):
        amount = items_to_add.count(item)
        if item in current_cart:
            current_cart[item] += amount
        else:
            current_cart[item] = amount
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    shopping_list = []
    
    for item in notes:
        shopping_list.append((item, 1))
    return dict(shopping_list)    

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    ideas |= recipe_updates
    return ideas

def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    dict_sorted = dict(sorted(cart.items()))
    return dict_sorted

def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    
    keeping_track_list = []

    for item in cart:
        if aisle_mapping[item]:
            keeping_track_list.append((item, [cart[item], *aisle_mapping[item]]))

    return dict(sorted(keeping_track_list, reverse=True))
            


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    for item in fulfillment_cart:
        if store_inventory[item]:
            store_inventory[item][0] -= fulfillment_cart[item][0]
    for item in store_inventory:
        if store_inventory[item][0] == 0:
            store_inventory[item][0] = 'Out of Stock'
    return store_inventory