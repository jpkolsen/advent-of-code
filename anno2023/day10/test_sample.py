from pathlib import Path

from .solution import part_one, part_two

LINES1 = Path(__file__).parent.joinpath("sample_input1.txt").read_text().splitlines()
LINES2 = Path(__file__).parent.joinpath("sample_input2.txt").read_text().splitlines()


def test_part_one():
    assert part_one(LINES1) == 4
    assert part_one(LINES2) == 8


def test_part_two():
    assert part_two(LINES1) == 0
    assert part_two(LINES2) == 0
