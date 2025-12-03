#!/usr/bin/env python3

"""Day 4: Ceres Search."""

import pathlib
import re


def get_diagonals(matrix: list) -> list:
    """
    Get matrix diagonals.

    >>> matrix = ['MMMSXXMASM',
    ... 'MSAMXMSMSA',
    ... 'AMXSXMAAMM',
    ... 'MSAMASMSMX',
    ... 'XMASAMXAMM',
    ... 'XXAMMXXAMA',
    ... 'SMSMSASXSS',
    ... 'SAXAMASAAA',
    ... 'MAMMMXMMMM',
    ... 'MXMXAXMASX']
    >>> get_diagonals(matrix)  # doctest: +NORMALIZE_WHITESPACE
    ['MSA', 'ASM', 'SAMM', 'MMMX', 'XMXSX', 'XSAMM', 'XXSAMX', 'XMASMA', 'MMXMAXS',
    'SXMMAMS', 'ASMASAMS', 'MMXSXASA', 'SMASAMSAM', 'MASAMXXAM', 'MSAMMMMXAM',
    'MSXMAXSAMX', 'AMSXXSAMX', 'MMASMASMS', 'MMAXAMMM', 'ASAMSAMA', 'XMASAMX',
    'MMAMMXM', 'MMXSXA', 'XXSAMX', 'ASAMX', 'XMXMA', 'SAMM', 'SAMX', 'AMA', 'SAM']
    """
    min_length = 3
    rows = len(matrix)
    cols = len(matrix[0])
    diagonals = []
    for i in range(rows + cols - 1):
        diag_lr = []
        diag_rl = []
        for row in range(rows):
            col_lr = i - row
            col_rl = cols - 1 - col_lr
            if 0 <= col_lr < cols:
                diag_lr.append(matrix[row][col_lr])
            if 0 <= col_rl < cols:
                diag_rl.append(matrix[row][col_rl])
        if len(diag_lr) >= min_length:
            diagonals.append("".join(diag_lr))
        if len(diag_lr) >= min_length:
            diagonals.append("".join(diag_rl))
    return diagonals


def get_columns(matrix: list) -> list:
    """
    Get matrix columns.

    >>> matrix = ['MMMSXXMASM',
    ... 'MSAMXMSMSA',
    ... 'AMXSXMAAMM',
    ... 'MSAMASMSMX',
    ... 'XMASAMXAMM',
    ... 'XXAMMXXAMA',
    ... 'SMSMSASXSS',
    ... 'SAXAMASAAA',
    ... 'MAMMMXMMMM',
    ... 'MXMXAXMASX']
    >>> get_columns(matrix)  # doctest: +NORMALIZE_WHITESPACE
    ['MMAMXXSSMM', 'MSMSMXMAAX', 'MAXAAASXMM', 'SMSMSMMAMX', 'XXXAAMSMMA',
    'XMMSMXAAXX', 'MSAMXXSSMM', 'AMASAAXAMA', 'SSMMMMSAMS', 'MAMXMASAMX']
    """
    return ["".join(col) for col in zip(*matrix, strict=True)]


def part1(matrix: list) -> int:
    """
    Part One.

    >>> matrix = ['MMMSXXMASM',
    ... 'MSAMXMSMSA',
    ... 'AMXSXMAAMM',
    ... 'MSAMASMSMX',
    ... 'XMASAMXAMM',
    ... 'XXAMMXXAMA',
    ... 'SMSMSASXSS',
    ... 'SAXAMASAAA',
    ... 'MAMMMXMMMM',
    ... 'MXMXAXMASX']
    >>> part1(matrix)
    18
    """
    lines = matrix + get_columns(matrix) + get_diagonals(matrix)
    lines += [line[::-1] for line in lines]
    pattern = re.compile(r"XMAS")
    return sum(len(pattern.findall(line)) for line in lines)


def part2(matrix: list) -> int:
    """
    Part Two.

    >>> matrix = ['MMMSXXMASM',
    ... 'MSAMXMSMSA',
    ... 'AMXSXMAAMM',
    ... 'MSAMASMSMX',
    ... 'XMASAMXAMM',
    ... 'XXAMMXXAMA',
    ... 'SMSMSASXSS',
    ... 'SAXAMASAAA',
    ... 'MAMMMXMMMM',
    ... 'MXMXAXMASX']
    >>> part2(matrix)
    9
    """
    pattern = re.compile(r"(M.S.A.M.S)|(M.M.A.S.S)")
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix = [row[j : j + 3] for row in matrix[i : i + 3]]
            substring = "".join("".join(row) for row in submatrix)
            for m in (substring, substring[::-1]):
                if pattern.match(m):
                    count += 1
    return count


def load_input(text: str) -> list:
    """
    Load input text.

    >>> text = '''MMMSXXMASM
    ... MSAMXMSMSA
    ... AMXSXMAAMM
    ... MSAMASMSMX
    ... XMASAMXAMM
    ... XXAMMXXAMA
    ... SMSMSASXSS
    ... SAXAMASAAA
    ... MAMMMXMMMM
    ... MXMXAXMASX'''
    >>> load_input(text)  # doctest: +NORMALIZE_WHITESPACE
    ['MMMSXXMASM',
    'MSAMXMSMSA',
    'AMXSXMAAMM',
    'MSAMASMSMX',
    'XMASAMXAMM',
    'XXAMMXXAMA',
    'SMSMSASXSS',
    'SAXAMASAAA',
    'MAMMMXMMMM',
    'MXMXAXMASX']
    """
    return text.splitlines()


if __name__ == "__main__":
    input_text = (pathlib.Path(__file__).parent / "input04").read_text().strip()
    values = load_input(input_text.strip())
    print(f"Part One: {part1(values)}")
    print(f"Part Two: {part2(values)}")
