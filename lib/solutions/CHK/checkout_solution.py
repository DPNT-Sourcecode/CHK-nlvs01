

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = [c for c in skus]
    for s in set(skus):
        quantity = skus.count(s)
        if s == 'E' and quantity / 2 > 0 and 'B' in skus:
            to_remove = quantity / 2
            for i in range(to_remove):
                if 'B' in skus:
                    skus.pop(skus.index('B'))
        if s == 'F' and quantity / 3 > 0:
            to_remove = quantity / 3
            for i in range(to_remove):
                if 'F' in skus:
                    skus.pop(skus.index('F'))
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
            prices.append(quantity * 20)
        elif s == 'D':
            prices.append(quantity * 15)
        elif s == 'E':
            prices.append(quantity * 40)
        elif s == 'F':
            prices.append(quantity * 10)
        else:
            return -1
    return sum(prices)


checkout('EEEB')
