

# noinspection PyUnusedLocal
# skus = unicode string


def calculate_offers(bill, item, quantity, offers):
    bill = bill.copy()
    for offer, price in offers:
        bill[item]['offers'].append(
            {'items': quantity / offer, 'price': price}
        )
        quantity = quantity % offer
    return bill, quantity


def get_free_item(bill, quantity, offer_quantity, free_item):
    bill = bill.copy()
    if free_item in bill:
        to_remove = quantity / offer_quantity
        new_quantity = bill[free_item]['standard']['items'] - to_remove
        if new_quantity > 0:
            bill[free_item]['standard']['items'] = new_quantity
        else:
            bill[free_item]['standard']['items'] = 0
    return bill

def process_bill(bill):
    bill_tot = list()
    for v in bill.values():
        standard_items = v['standard']['items']
        standard_price = v['standard']['price']
        bill_tot.append(standard_items * standard_price)
        item_offers = v['offers']
        for o in item_offers:
            items = o['items']
            price = o['price']
            bill_tot.append(items * price)
    return sum(bill_tot)

def checkout(skus):
    skus = sorted([c for c in skus])
    bill = dict()
    for s in set(skus):
        quantity = skus.count(s)
        unit_price = 0
        offers = tuple()
        offer_quantity = 0
        free_item = None
        bill[s] = {
            'standard':
                {'items': 0, 'price': 0},
            'offers': [],
        }
        if s == 'A':
            unit_price = 50
            offers = ((3, 130), (5, 200))
        elif s == 'B':
            unit_price = 30
            offers = ((2, 45),)
        elif s == 'C':
            unit_price = 20
        elif s == 'D':
            unit_price = 15
        elif s == 'E':
            offer_quantity = 2
            free_item = 'B'
            unit_price = 40
        elif s == 'F':
            offer_quantity = 3
            free_item = 'F'
            unit_price = 10
        elif s == 'G':
            unit_price = 20
        elif s == 'H':
            unit_price = 10
            offers = ((5, 45), (10, 80))
        elif s == 'I':
            unit_price = 35
        elif s == 'J':
            unit_price = 60
        elif s == 'K':
            unit_price = 80
            offers = ((2, 150),)
        elif s == 'L':
            unit_price = 90
        elif s == 'M':
            unit_price = 15
        elif s == 'N':
            unit_price = 40
            offer_quantity = 3
            free_item = 'M'
        elif s == 'O':
            unit_price = 10
        elif s == 'P':
            unit_price = 50
            offers = ((5, 200), )
        elif s == 'Q':
            unit_price = 30
            offers = ((3, 80),)
        elif s == 'R':
            unit_price = 50
            offer_quantity = 3
            free_item = 'Q'
        elif s == 'S':
            unit_price = 30
        elif s == 'T':
            unit_price = 20
        elif s == 'U':
            unit_price = 40
            offer_quantity = 3
            free_item = 'U'
        elif s == 'V':
            unit_price = 50
            offers = ((2, 90), (3, 130))
        elif s == 'W':
            unit_price = 20
        elif s == 'X':
            unit_price = 90
        elif s == 'Y':
            unit_price = 10
        elif s == 'Z':
            unit_price = 50
        else:
            return -1
        bill, quantity = calculate_offers(bill, s, quantity, offers)
        bill[s]['standard']['items'] = quantity
        bill[s]['standard']['price'] = unit_price
        bill = get_free_item(bill, quantity, offer_quantity, free_item)
    return process_bill(bill)
