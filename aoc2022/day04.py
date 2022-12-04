#!/usr/bin/env python3

"""Day 4: Camp Cleanup."""

import pathlib


def part1(pairs: list) -> int:
    """
    Part One.

    >>> pairs = [
    ...     [{2, 3, 4}, {6, 7, 8}],
    ...     [{2, 3}, {4, 5}],
    ...     [{5, 6, 7}, {7, 8, 9}],
    ...     [{2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}],
    ...     [{6}, {4, 5, 6}],
    ...     [{2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}],
    ... ]
    >>> part1(pairs)
    2
    """
    return sum(1 for a, b in pairs if a <= b or b <= a)


def part2(pairs: list) -> int:
    """
    Part Two.

    >>> pairs = [
    ...     [{2, 3, 4}, {6, 7, 8}],
    ...     [{2, 3}, {4, 5}],
    ...     [{5, 6, 7}, {7, 8, 9}],
    ...     [{2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}],
    ...     [{6}, {4, 5, 6}],
    ...     [{2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}],
    ... ]
    >>> part2(pairs)
    4
    """
    return sum(1 for a, b in pairs if a & b)


def load_input(input_text: str) -> list:
    """
    Load input text.

    >>> input_text = '''2-4,6-8
    ... 2-3,4-5
    ... 5-7,7-9
    ... 2-8,3-7
    ... 6-6,4-6
    ... 2-6,4-8'''
    >>> pairs = [
    ...     [{2, 3, 4}, {6, 7, 8}],
    ...     [{2, 3}, {4, 5}],
    ...     [{5, 6, 7}, {7, 8, 9}],
    ...     [{2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}],
    ...     [{6}, {4, 5, 6}],
    ...     [{2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}],
    ... ]
    >>> load_input(input_text) == pairs
    True
    """
    return [
        [
            set(range(*[int(i) + n for n, i in enumerate(a.split("-"))]))
            for a in r.split(",")
        ]
        for r in input_text.splitlines()
    ]


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input04").read_text()
    pairs = load_input(input_text.strip())
    print(f"Part One: {part1(pairs)}")
    print(f"Part Two: {part2(pairs)}")
