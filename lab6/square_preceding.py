"""task1.a"""

from doctest import testmod


def square_preceding(values):
    """ (list of number) -> NoneType
    Replace each item in the list with square the value of the
    preceding item, and replace the first item with 0.
    >>> L = [1, 2, 3]
    >>> print(square_preceding(L))
    [0, 1, 4]
    >>> L = []
    >>> print(square_preceding(L))
    []
    """

    if values != []:
        temp = values[0]
        values[0] = 0
    else:
        return []
    for i in range(1, len(values)):
        values[i], temp = temp ** 2, values[i]
    return values

if __name__ == "__main__":
    print(testmod())
