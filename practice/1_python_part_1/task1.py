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

"""Deletes specified item from the list."""
def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    for item in list_to_clean:
        if item == item_to_delete:
            index = list_to_clean.index(item)
            list_to_clean.pop(index)
    return list_to_clean