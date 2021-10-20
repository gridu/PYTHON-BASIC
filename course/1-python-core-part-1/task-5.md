Write function which receives line of space separated words.
Remove all duplicated words from line.
```
def remove_duplicated_words(line: str) -> str:
    ...
```

Examples:
```
>>> remove_duplicated_words('cat cat dog 1 dog 2')
'cat dog 1 2'

>>> remove_duplicated_words('cat cat cat')
'cat'

>>> remove_duplicated_words('1 2 3')
'1 2 3'
```