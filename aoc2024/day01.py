#!/usr/bin/env python3

"""Day 1: Historian Hysteria."""

import pathlib
from collections import Counter


def part1(values: tuple) -> int:
    """
    Part One.

    >>> values = ((3, 4, 2, 1, 3, 3), (4, 3, 5, 3, 9, 3))
    >>> part1(values)
    11
    """
    return sum(
        abs(a - b) for a, b in zip(sorted(values[0]), sorted(values[1]), strict=True)
    )


def part2(values: tuple) -> int:
    """
    Part Two.

    >>> values = ((3, 4, 2, 1, 3, 3), (4, 3, 5, 3, 9, 3))
    >>> part2(values)
    31
    """
    counter = Counter(values[1])
    return sum(a * counter[a] for a in values[0])


def load_input(text: str) -> tuple:
    """
    Load input text.

    >>> text = '''3   4
    ... 4   3
    ... 2   5
    ... 1   3
    ... 3   9
    ... 3   3'''
    >>> load_input(text)
    ((3, 4, 2, 1, 3, 3), (4, 3, 5, 3, 9, 3))
    """
    return tuple(
        zip(*(map(int, line.split()) for line in text.splitlines()), strict=True),
    )


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input01").read_text()
    values = load_input(input_text.strip())
    print(f"Part One: {part1(values)}")
    print(f"Part Two: {part2(values)}")
