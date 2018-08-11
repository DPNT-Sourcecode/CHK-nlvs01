

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
    skus = sorted([c for c in skus])
    bill = dict()
    for s in set(skus):
        quantity = skus.count(s)
        if s == 'A':
            if quantity / 5 > 0:
                bill[s] = {'offers': [
                    {'items': quantity / 5, 'price': 130}
                ]}
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