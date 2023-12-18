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
    try:
        index = list_to_clean.index(item_to_delete)
        list_to_clean.pop(index)
    except ValueError:
        pass  # The element to delete is not in the list
    return list_to_clean
