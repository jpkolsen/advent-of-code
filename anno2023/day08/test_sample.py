from pathlib import Path

from anno2023.day08.solution import part_one, part_two

LINES_1 = Path(__file__).parent.joinpath("sample_input1.txt").read_text().splitlines()
LINES_2 = Path(__file__).parent.joinpath("sample_input2.txt").read_text().splitlines()
LINES_3 = Path(__file__).parent.joinpath("sample_input3.txt").read_text().splitlines()


def test_part_one():
    assert part_one(LINES_1) == 2
    assert part_one(LINES_2) == 6


def test_part_two():
    assert part_two(LINES_3) == 6


if __name__ == "__main__":
    import time

    start_time = time.time()
    test_part_two()

    print(f"finsihed in {time.time() - start_time} seconds")
