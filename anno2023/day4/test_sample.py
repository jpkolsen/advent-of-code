import re
from pathlib import Path

from anno2023.day4.solution import part_one, part_two

LINES = Path(__file__).parent.joinpath("sample_input.txt").read_text().splitlines()


def test_part_one():
    assert part_one(LINES) == 0


def test_part_two():
    assert part_two(LINES) == 0
