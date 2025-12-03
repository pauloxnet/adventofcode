#!/usr/bin/env python3

"""Day 3: Rucksack Reorganization."""

import pathlib
import string

POINTS = {m: n for n, m in enumerate(string.ascii_letters, 1)}


def part1(rucksacks: list) -> int:
    """
    Part One.

    >>> rucksacks = [
    ...     'vJrwpWtwJgWrhcsFMMfFFhFp',
    ...     'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    ...     'PmmdzqPrVvPwwTWBwg',
    ...     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    ...     'ttgJtRGJQctTZtZT',
    ...     'CrZsJsPPZsGzwwsLwLmpwMDw'
    ... ]
    >>> part1(rucksacks)
    157
    """
    return sum(
        POINTS[next(iter(set(r[:d]) & set(r[d:])))]
        for r in rucksacks
        if (d := len(r) // 2)
    )


def part2(rucksacks: list) -> int:
    """
    Part Two.

    >>> rucksacks = [
    ...     'vJrwpWtwJgWrhcsFMMfFFhFp',
    ...     'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    ...     'PmmdzqPrVvPwwTWBwg',
    ...     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    ...     'ttgJtRGJQctTZtZT',
    ...     'CrZsJsPPZsGzwwsLwLmpwMDw'
    ... ]
    >>> part2(rucksacks)
    70
    """
    return sum(
        POINTS[
            next(
                iter(set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2])),
            )
        ]
        for i in range(0, len(rucksacks), 3)
    )


def load_input(input_text: str) -> list:
    """
    Load input text.

    >>> input_text = '''vJrwpWtwJgWrhcsFMMfFFhFp
    ... jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    ... PmmdzqPrVvPwwTWBwg
    ... wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ... ttgJtRGJQctTZtZT
    ... CrZsJsPPZsGzwwsLwLmpwMDw'''
    >>> load_input(input_text)  # doctest: +NORMALIZE_WHITESPACE
    ['vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw']
    """
    return input_text.splitlines()


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input03").read_text()
    rucksacks = load_input(input_text.strip())
    print(f"Part One: {part1(rucksacks)}")
    print(f"Part Two: {part2(rucksacks)}")
