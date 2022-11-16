from typing import Dict


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    for key in items_to_set:
        if items_to_set[key] > dict_to_update.get(key, float('-inf')):
            dict_to_update[key] = items_to_set[key]
    return dict_to_update


if __name__ == '__main__':
    print(set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4))
    print(set_to_dict({}, a=0))
    print(set_to_dict({'a': 5}))
