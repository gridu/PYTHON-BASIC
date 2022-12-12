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
    for i in dict_to_update:
        pass
      #  print (dict_to_update[i])
    if len(dict_to_update) == 0: 
        return(items_to_set)
    else:
        for i in items_to_set:
            if (dict_to_update.get(i))<(items_to_set[i]):
                dict_to_update[i]=items_to_set[i]
        return(dict_to_update)
        
set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)
