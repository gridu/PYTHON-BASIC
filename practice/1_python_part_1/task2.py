"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    for item in items_to_set:
        if item in dict_to_update:
            if items_to_set[item] > dict_to_update[item]:
                dict_to_update[item] = items_to_set[item]
        else:
            dict_to_update[item] =  items_to_set[item]
    return dict_to_update

# test 2 requires "a" as a key {a:0}