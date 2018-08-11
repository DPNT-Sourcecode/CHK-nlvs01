# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if all(0 <= n <= 100 for n in (x, y)):
        return x + y
    else:
        raise ValueError('Please provide two integer numbers')
