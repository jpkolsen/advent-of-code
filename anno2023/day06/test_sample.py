from pathlib import Path

from anno2023.day06.solution import Race, parse_races, part_one, part_two

LINES = Path(__file__).parent.joinpath("sample_input.txt").read_text().splitlines()


def test_parser():
    assert parse_races(LINES) == ([7, 15, 30], [9, 40, 200])


def test_calculator():
    assert Race(7, 9).beat_times == (2, 5)
    assert Race(15, 40).beat_times == (4, 11)
    assert Race(30, 200).beat_times == (11, 19)


def test_part_one():
    assert part_one(LINES) == 288


def test_part_two():
    assert part_two(LINES) == 71503


if __name__ == "__main__":
    test_part_two()
