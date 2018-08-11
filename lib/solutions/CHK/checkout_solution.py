

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus_lookup = {
        'A': {
            'price': 50,
            'offer': {
                'items': 3,
                'price': 130
            }
        },
        'B': {
            'price': 30,
            'offer': {
                'items': 2,
                'price': 45
            }
        },
        'C': {
            'price': 20
        },
        'D': {
            'price': 15
        },

    }
    prices = []
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
