import collections
from random import choice

def get_random_item(sample):
    """Return a random choice of a sample
    If single element passed it is returned
    """
    if isinstance(sample, collections.Iterable):
        return choice(sample)
    else:
        return sample
