#!/usr/bin/env python3

"""Day 4: Scratchcards."""

import pathlib
import re


def part1(values: dict) -> int:
    """
    Part One.

    >>> values = {1: [1, {41, 48, 17, 83, 86}, {6, 9, 48, 17, 83, 53, 86, 31}],
    ... 2: [1, {32, 13, 16, 20, 61}, {32, 68, 17, 82, 19, 24, 61, 30}],
    ... 3: [1, {1, 44, 53, 21, 59}, {1, 69, 72, 14, 16, 82, 21, 63}],
    ... 4: [1, {69, 73, 41, 84, 92}, {5, 76, 51, 84, 83, 54, 58, 59}],
    ... 5: [1, {32, 83, 87, 26, 28}, {36, 70, 12, 82, 22, 88, 93, 30}],
    ... 6: [1, {72, 13, 18, 56, 31}, {35, 67, 36, 74, 10, 11, 77, 23}]}
    >>> part1(values)
    13
    """
    points = 0
    for parts in values.values():
        winners = len(parts[1].intersection(parts[2]))
        if winners > 0:
            points += 2 ** (winners - 1)
    return points


def part2(values: dict) -> int:
    """
    Part Two.

    >>> values = {1: [1, {41, 48, 17, 83, 86}, {6, 9, 48, 17, 83, 53, 86, 31}],
    ... 2: [1, {32, 13, 16, 20, 61}, {32, 68, 17, 82, 19, 24, 61, 30}],
    ... 3: [1, {1, 44, 53, 21, 59}, {1, 69, 72, 14, 16, 82, 21, 63}],
    ... 4: [1, {69, 73, 41, 84, 92}, {5, 76, 51, 84, 83, 54, 58, 59}],
    ... 5: [1, {32, 83, 87, 26, 28}, {36, 70, 12, 82, 22, 88, 93, 30}],
    ... 6: [1, {72, 13, 18, 56, 31}, {35, 67, 36, 74, 10, 11, 77, 23}]}
    >>> part2(values)
    30
    """
    for key, parts in values.items():
        winners = len(parts[1].intersection(parts[2]))
        if winners > 0:
            for i in range(1, winners + 1):
                values[key + i][0] += 1 * parts[0]
    return sum(v[0] for v in values.values())


def load_input(input_text: str) -> dict:
    """
    Load input text.

    >>> input_text = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    ... Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    ... Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    ... Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    ... Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    ... Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
    >>> load_input(input_text)  # doctest: +NORMALIZE_WHITESPACE
    {1: [1, {41, 48, 17, 83, 86}, {6, 9, 48, 17, 83, 53, 86, 31}],
    2: [1, {32, 13, 16, 20, 61}, {32, 68, 17, 82, 19, 24, 61, 30}],
    3: [1, {1, 44, 53, 21, 59}, {1, 69, 72, 14, 16, 82, 21, 63}],
    4: [1, {69, 73, 41, 84, 92}, {5, 76, 51, 84, 83, 54, 58, 59}],
    5: [1, {32, 83, 87, 26, 28}, {36, 70, 12, 82, 22, 88, 93, 30}],
    6: [1, {72, 13, 18, 56, 31}, {35, 67, 36, 74, 10, 11, 77, 23}]}
    """
    scratchcards = {}
    for line in input_text.split("\n"):
        card, lists = line.split(": ")
        card_id = int(card[5:])
        numbers, winners = lists.split(" | ")
        numbers_set = set(map(int, re.findall(r"\d+", numbers)))
        winners_set = set(map(int, re.findall(r"\d+", winners)))
        scratchcards[card_id] = [1, numbers_set, winners_set]
    return scratchcards


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input04").read_text()
    values = load_input(input_text.strip())
    print(f"Part One: {part1(values)}")
    print(f"Part Two: {part2(values)}")
