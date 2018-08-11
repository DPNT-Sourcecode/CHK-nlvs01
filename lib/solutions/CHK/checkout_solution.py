

# noinspection PyUnusedLocal
# skus = unicode string

def get_free_items(skus_items, offer_type, offer_quantity, free_item):
    """
    :param skus_item: skus items list
    :param offer_type: the type of item that defines the offer
    :param offer_quantity: the quanity of the item that defines the offer
    :param free_item: the item to remove from skus_items
    :return: new skus_items list without the items on offer
    """
    to_remove = offer_quantity / 2
    for i in range(to_remove):
        if free_item in skus_items:
            skus_items.pop(skus_items.index(free_item))
    return skus_items


def checkout(skus):
    skus = [c for c in skus]
    # items to remove
    for s in set(skus):
        quantity = skus.count(s)
        if s == 'E' and quantity / 2 > 0 and 'B' in skus:
            skus = get_free_items(skus, 'E', 2, 'B')
        if s == 'F' and quantity / 3 > 0:
            skus = get_free_items(skus, 'F', 3, 'F')
        if s == 'N' and quantity / 3 > 0 and 'M' in skus:
            skus = get_free_items(skus, 'N', 3, 'M')
        if s == 'R' and quantity / 3 > 0 and 'Q' in skus:
            skus = get_free_items(skus, 'R', 3, 'Q')
        if s == 'U' and quantity / 3 > 0:
            skus = get_free_items(skus, 'U', 3, 'U')

    prices = []
    for s in set(skus):
        quantity = skus.count(s)
        if s == 'A':
            offer_five = 0
            offer_three = 0
            while quantity >= 3:
                if quantity / 5 > 0:
                    offer_five = quantity / 5
                    quantity = quantity % 5
                if quantity / 3 > 0:
                    offer_three = quantity / 3
                    quantity = quantity % 3
            prices.append(sum([offer_five * 200, offer_three * 130, quantity * 50]))
        elif s == 'B':
            offer_two = 0
            if quantity >= 2:
                offer_two = quantity / 2
                quantity = quantity % 2
            prices.append(sum([offer_two * 45, quantity * 30]))
        elif s == 'C':
            unit_price = 20
            tot_price = unit_price
        elif s == 'D':
            unit_price = 15
        elif s == 'E':
            unit_price = 40
        elif s == 'F':
            unit_price = 10
        elif s == 'G':
            unit_price = 20
        elif s == 'F':
            unit_price = 10

        else:
            return -1
    return sum(prices)


checkout('EEEB')
