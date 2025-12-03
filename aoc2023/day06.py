#!/usr/bin/env python3

"""Day 6: Wait For It."""

import pathlib
import re


def get_wins(times: list) -> int:
    """
    Get wins from times.

    >>> times = [(7, 9), (15, 40), (30, 200)]
    >>> get_wins(times)
    288
    >>> times = [(71530, 940200)]
    >>> get_wins(times)
    71503
    """
    wins = 1
    for time, distance in times:
        wins *= len([r for t in range(time + 1) if (r := t * (time - t)) > distance])
    return wins


def part1(values: list) -> int:
    """
    Part One.

    >>> values = ['7  15   30', '9  40  200']
    >>> part1(values)
    288
    """
    times = list(zip(*(map(int, re.findall(r"\d+", v)) for v in values), strict=True))
    return get_wins(times)


def part2(values: list) -> int:
    """
    Part Two.

    >>> values = ['7  15   30', '9  40  200']
    >>> part2(values)
    71503
    """
    times = [(int(d.replace(" ", "")) for d in values)]
    return get_wins(times)


def load_input(input_text: str) -> list:
    """
    Load input text.

    >>> input_text = '''Time:      7  15   30
    ... Distance:  9  40  200'''
    >>> load_input(input_text)
    ['7  15   30', '9  40  200']
    """
    return [line[9:].strip() for line in input_text.split("\n")]


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input06").read_text()
    values = load_input(input_text.strip())
    print(f"Part One: {part1(values)}")
    print(f"Part Two: {part2(values)}")
