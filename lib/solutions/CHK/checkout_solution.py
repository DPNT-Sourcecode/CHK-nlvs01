

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for s in set(skus):
        quantity = skus.count(s)
        if s == 'E' and quantity % 2 == 0 and 'B' in skus:
            to_remove = quantity / 2
            for i in range(to_remove):
                if 'B' in skus:
                    skus.pop('B')
    prices = []
    for s in set(skus):
        quantity = skus.count(s)
        if s == 'A':
            if quantity > 5:
                on_offer = quantity / 5





    return sum(prices)
