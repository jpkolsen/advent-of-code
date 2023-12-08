from pathlib import Path
import re

from anno2023.day3.solution import part_one, SYMBOLS, SYMBOLS_REGEX, LINES


def test_regex():
    assert [m.start() for m in re.finditer(SYMBOLS_REGEX, "ab+cd*")] == [2, 5]


def test_sample_input():
    lines = Path(__file__).parent.joinpath("sample_input.txt").read_text().splitlines()
    print(*lines, end="\n")
    assert part_one(lines) == 4361
