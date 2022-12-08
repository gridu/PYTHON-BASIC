
import typing


class DivisionByOneException(Exception):
    """You will get the same result"""
    pass


def division(x: int, y: int) -> typing.Union[None, int]:
    if y == 0:
        print('Division by 0')
        print('Division finished')
    elif y == 1:
        print('Division finished')
        raise DivisionByOneException("Deletion on 1 get the same result")
    else:
        print('Division finished')
        return x/y
    return None


if __name__ == '__main__':
    print(division(1, 0))
    print(division(2, 2))
    print(division(1, 1))