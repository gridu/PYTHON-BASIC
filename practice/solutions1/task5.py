from task3 import unique_list


def remove_duplicated_words(line: str) -> str:
    return ' '.join(unique_list(line.split()))


if __name__ == '__main__':
    print(remove_duplicated_words('cat cat dog 1 dog 2'))
    print(remove_duplicated_words('cat cat cat'))
    print(remove_duplicated_words('1 2 3'))
