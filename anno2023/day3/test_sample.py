import re
from pathlib import Path

from anno2023.day3.solution import SYMBOLS_REGEX, part_one, part_two


def test_regex():
    assert [m.start() for m in re.finditer(SYMBOLS_REGEX, "ab+cd*")] == [2, 5]


def test_part_one():
    lines = Path(__file__).parent.joinpath("sample_input.txt").read_text().splitlines()
    assert part_one(lines) == 4361


def test_part_two():
    lines = Path(__file__).parent.joinpath("sample_input.txt").read_text().splitlines()
    assert part_two(lines) == 467835
