#!/usr/bin/env python3

"""Day 2: Red-Nosed Reports."""

import pathlib
from itertools import combinations, pairwise


def is_safe(row: tuple) -> bool:
    """Check if the row is safe.

    >>> is_safe((7, 6, 4, 2, 1))
    True
    >>> is_safe((1, 2, 7, 8, 9))
    False
    >>> is_safe((9, 7, 6, 2, 1))
    False
    >>> is_safe((1, 3, 2, 4, 5))
    False
    >>> is_safe((8, 6, 4, 4, 1))
    False
    >>> is_safe((1, 3, 6, 7, 9))
    True
    """
    top = 3
    pdiff = 0
    for a, b in pairwise(row):
        if ((diff := b - a) * pdiff < 0) or ((adiff := abs(diff)) > top) or (adiff < 1):
            return False
        pdiff = diff
    return True


def part1(values: tuple) -> int:
    """Part One.

    >>> values = ((7, 6, 4, 2, 1),
    ... (1, 2, 7, 8, 9),
    ... (9, 7, 6, 2, 1),
    ... (1, 3, 2, 4, 5),
    ... (8, 6, 4, 4, 1),
    ... (1, 3, 6, 7, 9))
    >>> part1(values)
    2
    """
    return sum(1 for value in values if is_safe(value))


def part2(values: tuple) -> int:
    """Part Two.

    >>> values = ((7, 6, 4, 2, 1),
    ... (1, 2, 7, 8, 9),
    ... (9, 7, 6, 2, 1),
    ... (1, 3, 2, 4, 5),
    ... (8, 6, 4, 4, 1),
    ... (1, 3, 6, 7, 9))
    >>> part2(values)
    4
    """
    result = 0
    for value in values:
        if is_safe(value):
            result += 1
        else:
            for combined_value in combinations(value, len(value) - 1):
                if is_safe(combined_value):
                    result += 1
                    break
    return result


def load_input(text: str) -> tuple:
    """Load input text.

    >>> text = '''7 6 4 2 1
    ... 1 2 7 8 9
    ... 9 7 6 2 1
    ... 1 3 2 4 5
    ... 8 6 4 4 1
    ... 1 3 6 7 9'''
    >>> load_input(text)  # doctest: +NORMALIZE_WHITESPACE
    ((7, 6, 4, 2, 1),
    (1, 2, 7, 8, 9),
    (9, 7, 6, 2, 1),
    (1, 3, 2, 4, 5),
    (8, 6, 4, 4, 1),
    (1, 3, 6, 7, 9))
    """
    return tuple(tuple(map(int, line.split())) for line in text.splitlines())


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input02").read_text()
    values = load_input(input_text.strip())
    print(f"Part One: {part1(values)}")
    print(f"Part Two: {part2(values)}")
