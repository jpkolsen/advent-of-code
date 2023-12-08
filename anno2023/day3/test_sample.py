from pathlib import Path

from anno2023.day3.solution import part_one


def test_sample_input():
    lines = Path(__file__).parent.joinpath("sample_input.txt").read_text().splitlines()

    assert part_one(lines) == 4361
