from pathlib import Path

from .solution import part_one, part_two

LINES1 = Path(__file__).parent.joinpath("sample_input1.txt").read_text().splitlines()
LINES2 = Path(__file__).parent.joinpath("sample_input2.txt").read_text().splitlines()


def test_start_pos():
    array = LINES1
    start_pos = [(i, l.find("S")) for i, l in enumerate(array) if l.find("S") > -1]
    assert start_pos == [(1, 1)]

    assert array[1][1] == "S"

    array = LINES2
    start_pos = [(i, l.find("S")) for i, l in enumerate(array) if l.find("S") > -1]
    assert start_pos == [(2, 0)]

    assert array[2][0] == "S"


def test_part_one():
    assert part_one(LINES1) == 4
    assert part_one(LINES2) == 8


def test_part_two():
    assert part_two(LINES1) == 0
    assert part_two(LINES2) == 0


if __name__ == "__main__":
    test_part_one()
