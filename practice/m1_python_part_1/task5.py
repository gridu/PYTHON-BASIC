"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    tab = line.split()
    unique_tab = list(dict.fromkeys(tab))
    final_str = " ".join(unique_tab)
    return final_str


if __name__ == "__main__":
    print(remove_duplicated_words("cat cat dog 1 dog 2"))
    print(remove_duplicated_words("cat cat cat"))
    print(remove_duplicated_words("1 2 3"))
