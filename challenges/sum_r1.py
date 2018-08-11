
def sum_integers(x, y):

    """
    :param x: an integer number
    :param y: an integer number
    :return: sum of x + y
    """
    if all(isinstance(n, int) for n in (x, y)):
        return x + y
    else:
        raise ValueError('Please provide two integer numbers')
