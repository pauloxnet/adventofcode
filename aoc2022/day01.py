#!/usr/bin/env python3

"""Day 1: Calorie Counting."""

import pathlib


def part1(cals: list) -> int:
    """
    Part One.

    >>> cals = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    >>> part1(cals)
    24000
    """
    return max([sum(c) for c in cals])


def part2(cals: list) -> int:
    """
    Part Two.

    >>> cals = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    >>> part2(cals)
    45000
    """
    return sum(sorted(sum(c) for c in cals)[-3:])


def load_input(input_text: str) -> list:
    """
    Load input text.

    >>> input_text = '''1000
    ... 2000
    ... 3000
    ...
    ... 4000
    ...
    ... 5000
    ... 6000
    ...
    ... 7000
    ... 8000
    ... 9000
    ...
    ... 10000'''
    >>> load_input(input_text)
    [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    """
    return [[int(n) for n in g.split("\n")] for g in input_text.split("\n\n")]


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input01").read_text()
    cals = load_input(input_text.strip())
    print(f"Part One: {part1(cals)}")
    print(f"Part Two: {part2(cals)}")
