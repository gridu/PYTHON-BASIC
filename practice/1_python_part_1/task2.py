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
    if dict_to_update == {}:
        return items_to_set
    elif items_to_set == {}:
        return dict_to_update
    else:
        for x in dict_to_update.keys():
            for y in items_to_set.keys():
                if x == y:
                    currentvalue = dict_to_update.get(x)
                    newvalue = items_to_set.get(y)
                    dict_to_update[x] = newvalue if currentvalue < newvalue else currentvalue
        return dict_to_update


