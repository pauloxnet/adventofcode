#!/usr/bin/env python3

"""Day 2: Cube Conundrum."""

import math
import pathlib


def part1(values: dict) -> int:
    """
    Part One.

    >>> values = {1: {'red': 4, 'green': 2, 'blue': 6},
    ... 2: {'red': 1, 'green': 3, 'blue': 4},
    ... 3: {'red': 20, 'green': 13, 'blue': 6},
    ... 4: {'red': 14, 'green': 3, 'blue': 15},
    ... 5: {'red': 6, 'green': 3, 'blue': 2}}
    >>> part1(values)
    8
    """
    bag = (12, 13, 14)
    return sum(
        k
        for k, v in values.items()
        if all(x <= y for x, y in zip(v.values(), bag, strict=True))
    )


def part2(values: dict) -> int:
    """
    Part Two.

    >>> values = {1: {'red': 4, 'green': 2, 'blue': 6},
    ... 2: {'red': 1, 'green': 3, 'blue': 4},
    ... 3: {'red': 20, 'green': 13, 'blue': 6},
    ... 4: {'red': 14, 'green': 3, 'blue': 15},
    ... 5: {'red': 6, 'green': 3, 'blue': 2}}
    >>> part2(values)
    2286
    """
    return sum(math.prod(v.values()) for v in values.values())


def load_input(input_text: str) -> dict:
    """
    Load input text.

    >>> input_text = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    ... Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    ... Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    ... Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    ... Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
    >>> load_input(input_text)  # doctest: +NORMALIZE_WHITESPACE
    {1: {'red': 4, 'green': 2, 'blue': 6},
    2: {'red': 1, 'green': 3, 'blue': 4},
    3: {'red': 20, 'green': 13, 'blue': 6},
    4: {'red': 14, 'green': 3, 'blue': 15},
    5: {'red': 6, 'green': 3, 'blue': 2}}
    """
    games = {}
    for line in input_text.split("\n"):
        k, e = line.split(": ")
        pk = int(k[5:])
        games[pk] = {"red": 0, "green": 0, "blue": 0}
        for v in e.split("; "):
            for c in v.split(", "):
                n, h = c.split(" ")
                if (m := int(n)) > games[pk][h]:
                    games[pk][h] = m
    return games


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input02").read_text()
    values = load_input(input_text.strip())
    print(f"Part One: {part1(values)}")
    print(f"Part Two: {part2(values)}")
