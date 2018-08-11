

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if isinstance(friend_name, str):
        return "Hello {}".format(friend_name)
    else:
        raise ValueError('Please provide a string')
