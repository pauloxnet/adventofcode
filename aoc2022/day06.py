#!/usr/bin/env python3

"""Day 6: Tuning Trouble."""

import pathlib


def get_distinct_characters_index(datastream: str, distinctnumber: int) -> int:
    """
    Get the first distinct characters index in datastream.

    >>> datastream = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    >>> get_distinct_characters_index(datastream, 2)
    -1
    >>> datastream = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    >>> get_distinct_characters_index(datastream, 4)
    7
    >>> datastream = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    >>> get_distinct_characters_index(datastream, 14)
    19
    """
    distinct_characters_index = -1
    for i in range(len(datastream)):
        if len(set(datastream[i : i + distinctnumber])) == distinctnumber:
            distinct_characters_index = i + distinctnumber
            break
        else:
            continue
    return distinct_characters_index


def part1(datastream: str) -> int:
    """
    Part One.

    >>> datastream = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    >>> part1(datastream)
    7
    >>> datastream = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
    >>> part1(datastream)
    5
    >>> datastream = 'nppdvjthqldpwncqszvftbrmjlhg'
    >>> part1(datastream)
    6
    >>> datastream = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
    >>> part1(datastream)
    10
    >>> datastream = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
    >>> part1(datastream)
    11
    """
    return get_distinct_characters_index(datastream, 4)


def part2(datastream) -> int:
    """
    Part Two.

    >>> datastream = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    >>> part2(datastream)
    19
    >>> datastream = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
    >>> part2(datastream)
    23
    >>> datastream = 'nppdvjthqldpwncqszvftbrmjlhg'
    >>> part2(datastream)
    23
    >>> datastream = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
    >>> part2(datastream)
    29
    >>> datastream = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
    >>> part2(datastream)
    26
    """
    return get_distinct_characters_index(datastream, 14)


if __name__ == "__main__":
    datastream = (pathlib.Path(__file__).parent / "input06").read_text().strip()
    print(f"Part One: {part1(datastream)}")
    print(f"Part Two: {part2(datastream)}")
