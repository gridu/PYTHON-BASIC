"""
Write function which deletes defined element from list.
Restriction: Use .pop method of list to remove item.
Examples:
    >>> delete_from_list([1, 2, 3, 4, 3], 3)
    [1, 2, 4]
    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    ['a', 'c', 'd']
    >>> delete_from_list([1, 2, 3], 'b')
    [1, 2, 3]
    >>> delete_from_list([], 'b')
    []
"""
from typing import List, Any


def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    '''
    using .remove
        while True:
        try:
            list_to_clean.remove(item_to_delete)
        except ValueError:
            break
    '''
    to_del = []
    for i in range(len(list_to_clean)):
        if list_to_clean[i] == item_to_delete:
            to_del.append(i)
    counter = 0
    for i in to_del:
        list_to_clean.pop(i-counter)
        counter += 1
    return list_to_clean

