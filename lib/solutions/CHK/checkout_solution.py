

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


def remove_free_items(skus):
    def remove_free_item(quantity, offer_quantity, free_item):
        to_remove = quantity / offer_quantity
        for t in range(to_remove):
            if free_item in skus:
                skus.pop(skus.index(free_item))
    for s in set(skus):
        quantity = skus.count(s)
        if s == 'E':
            offer_quantity = 2
            free_item = 'B'
        elif s == 'F':
            offer_quantity = 3
            free_item = 'F'
        elif s == 'N':
            offer_quantity = 3
            free_item = 'M'
        elif s == 'R':
            offer_quantity = 3
            free_item = 'Q'
        elif s == 'U':
            offer_quantity = 4
            free_item = 'U'
        else:
            continue
        remove_free_item(quantity, offer_quantity, free_item)
    return skus


def any_of_three(skus, bill):
    def pop_items(items_to_pop):
        for i in items_to_pop:
            skus.pop(skus.index(i))
    count = 0
    tot = 0
    to_pop = []
    last_item = None
    for item in skus:
        if item in 'STXYZ':
            bill[item] = {
                'standard':
                    {'items': 0, 'price': 0},
                'offers': [],
            }
            count += 1
            to_pop.append(item)
        if count == 3:
            count = 0
            tot += 1
            pop_items(to_pop)
            last_item = item
    if last_item is not None:
        bill[last_item]['offers'].append({'items': tot, 'price': 45})
    return skus, bill

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
    skus = remove_free_items(skus)
    skus, bill = any_of_three(skus, bill)
    for s in set(skus):
        quantity = skus.count(s)
        offers = tuple()
        bill[s] = {
            'standard':
                {'items': 0, 'price': 0},
            'offers': [],
        }
        if s == 'A':
            unit_price = 50
            offers = ((5, 200), (3, 130))
        elif s == 'B':
            unit_price = 30
            offers = ((2, 45),)
        elif s == 'C':
            unit_price = 20
        elif s == 'D':
            unit_price = 15
        elif s == 'E':
            unit_price = 40
        elif s == 'F':
            unit_price = 10
        elif s == 'G':
            unit_price = 20
        elif s == 'H':
            unit_price = 10
            offers = ((10, 80), (5, 45))
        elif s == 'I':
            unit_price = 35
        elif s == 'J':
            unit_price = 60
        elif s == 'K':
            unit_price = 70
            offers = ((2, 120),)
        elif s == 'L':
            unit_price = 90
        elif s == 'M':
            unit_price = 15
        elif s == 'N':
            unit_price = 40
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
        elif s == 'S':
            unit_price = 20
        elif s == 'T':
            unit_price = 20
        elif s == 'U':
            unit_price = 40
        elif s == 'V':
            unit_price = 50
            offers = ((3, 130), (2, 90))
        elif s == 'W':
            unit_price = 20
        elif s == 'X':
            unit_price = 17
        elif s == 'Y':
            unit_price = 20
        elif s == 'Z':
            unit_price = 21
        else:
            return -1
        bill, quantity = calculate_offers(bill, s, quantity, offers)
        bill[s]['standard']['items'] = quantity
        bill[s]['standard']['price'] = unit_price

    return process_bill(bill)


checkout('STX')
