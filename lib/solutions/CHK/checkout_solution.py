

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus_lookup = {
        'A': {
            'price': 50,
            'offers': {
                3: 130,
                5: 200,
            }
        },
        'B': {
            'price': 30,
            'offers': {
                2: 45
            }
        },
        'C': {
            'price': 20
        },
        'D': {
            'price': 15
        },
        'E': {
            'price': 40
        },

    }
    multi_prices_lookup = {
        'E': {
            'quantity': 2,
            'item': 'B'
        }
    }
    prices = []
    for s in set(skus):
        if s in multi_prices_lookup:
            free_item = multi_prices_lookup[s]['item']
            if free_item in skus:
                quantity = skus.count(s)
                if quantity >= multi_prices_lookup[s]['quantity']:
                    to_remove = quantity / multi_prices_lookup[s]['quantity']
                    for t in range(to_remove):
                        if free_item in skus:
                            skus.pop(free_item)
    for s in set(skus):
        quantity = skus.count(s)
        if s in skus_lookup:
            item = skus_lookup[s]
            item_price = 0
            if 'offer' in item:
                if quantity >= item['offer']['items']:
                    offer_items = quantity / item['offer']['items']
                    normal_items = quantity % item['offer']['items']
                    offer_price = offer_items * item['offer']['price']
                    normal_price = normal_items * item['price']
                    item_price = sum([normal_price, offer_price])
                else:
                    item_price = item['price'] * quantity
            else:
                item_price = item['price'] * quantity
            prices.append(item_price)
        else:
            return -1
    return sum(prices)
