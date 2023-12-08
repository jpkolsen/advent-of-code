from pathlib import Path

from .solution import part_one


def test_sample_input():
    lines = Path(__file__).parent.joinpath("sample.txt").read_text().splitlines()

    assert part_one(lines) == 4361
