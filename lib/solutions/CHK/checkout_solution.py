

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
        return skus
    count = 0
    tot = 0
    to_pop = []
    last_item = None
    while skus:
        for item in skus:
            if item in 'STXYZ':
                if item not in bill:
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
                skus = pop_items(to_pop)
                to_pop = []
                last_item = item
                continue
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
    return 1


checkout("")