from typing import Iterable


def unique_list(seq: Iterable) -> list:
    unique = []
    for i in seq:
        if i not in unique:
            unique.append(i)
    return unique


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    uniques = []
    for i in range(len(lines)):
        if len(lines[i]) > 0:
            uniques.append(unique_list(lines[i].split()))
    uniques = [unique[word_number] for unique in uniques if word_number < len(unique)]
    return " ".join(uniques)


if __name__ == '__main__':
    print(build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1))
    print(build_from_unique_words('a b c', '', 'cat dog milk', word_number=0))
    print(build_from_unique_words('1 2', '1 2 3', word_number=10))
    print(build_from_unique_words(word_number=10))