
def sum(x, y):

    """
    !!Function name is shadowing built in sum!!
    :param x: an integer number between 0 and 100
    :param y: an integer number between 0 and 100
    :return: sum of x + y
    """
    if all(isinstance(n, int) for n in (x, y)) and all(0 <= n <= 100 for n in (x, y)):
        return x + y
    else:
        raise ValueError('Please provide two integer numbers')
