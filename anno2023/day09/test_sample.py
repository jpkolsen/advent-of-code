from pathlib import Path

from anno2023.day09.solution import part_one, part_two

LINES = Path(__file__).parent.joinpath("sample_input.txt").read_text().splitlines()


def test_part_one():
    assert part_one(LINES) == 114


def test_part_two():
    assert part_two(LINES) == 0


if __name__ == "__main__":
    test_part_one()
