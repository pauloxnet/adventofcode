#!/usr/bin/env python3

"""Day 1: Trebuchet?!."""

import pathlib
import re

ALPHADIGITS = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
REDIGITS = re.compile(r"\d")
REALPHADIGITS = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")


def part1(values: list) -> int:
    """
    Part One.

    >>> values = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    >>> part1(values)
    142
    """
    return sum(get_calibration_value(v, REDIGITS) for v in values)


def part2(values: list) -> int:
    """
    Part Two.

    >>> values = [
    ... 'two1nine',
    ... 'eightwothree',
    ... 'abcone2threexyz',
    ... 'xtwone3four',
    ... '4nineeightseven2',
    ... 'zoneight234',
    ... '7pqrstsixteen'
    ... ]
    >>> part2(values)
    281
    """
    return sum(get_calibration_value(v, REALPHADIGITS) for v in values)


def get_calibration_value(line: str, regex: re.Pattern[str]) -> int:
    """
    Get calibration value.

    >>> get_calibration_value('1abc2', REDIGITS)
    12
    >>> get_calibration_value('pqr3stu8vwx', REDIGITS)
    38
    >>> get_calibration_value('a1b2c3d4e5f', REDIGITS)
    15
    >>> get_calibration_value('treb7uchet', REDIGITS)
    77
    >>> get_calibration_value('two1nine', REALPHADIGITS)
    29
    >>> get_calibration_value('eightwothree', REALPHADIGITS)
    83
    >>> get_calibration_value('abcone2threexyz', REALPHADIGITS)
    13
    >>> get_calibration_value('xtwone3four', REALPHADIGITS)
    24
    >>> get_calibration_value('4nineeightseven2', REALPHADIGITS)
    42
    >>> get_calibration_value('zoneight234', REALPHADIGITS)
    14
    >>> get_calibration_value('7pqrstsixteen', REALPHADIGITS)
    76
    >>> get_calibration_value('nineight', REALPHADIGITS)
    98
    """
    occurrences = regex.findall(line)
    return int(ALPHADIGITS[occurrences[0]] + ALPHADIGITS[occurrences[-1]])


def load_input(input_text: str) -> list:
    """
    Load input text.

    >>> input_text = '''1abc2
    ... pqr3stu8vwx
    ... a1b2c3d4e5f
    ... treb7uchet'''
    >>> load_input(input_text)
    ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    """
    return input_text.split("\n")


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input01").read_text()
    values = load_input(input_text.strip())
    print(f"Part One: {part1(values)}")
    print(f"Part Two: {part2(values)}")
