#!/usr/bin/env python3

"""Day 3: Mull It Over."""

import math
import pathlib
import re


def part1(text: str) -> int:
    """Part One.

    >>> tx = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    >>> part1(tx)
    161
    """
    return sum(math.prod(map(int, m)) for m in re.findall(r"mul\((\d+),(\d+)\)", text))


def part2(text: str) -> int:
    """Part Two.

    >>> tx = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    >>> part2(tx)
    48
    """
    return sum(
        sum(math.prod(map(int, m)) for m in re.findall(r"mul\((\d+),(\d+)\)", s))
        for s in re.findall(r"do\(\)(.*?)(?=don't\(\)|$)", "do()" + text, re.DOTALL)
    )


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input03").read_text().strip()
    print(f"Part One: {part1(input_text)}")
    print(f"Part Two: {part2(input_text)}")
