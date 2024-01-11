from pathlib import Path

from .solution import part_one, part_two

ARRAYS = []
for file in [f"sample_input{i}.txt" for i in range(1, 6)]:
    ARRAYS.append(Path(__file__).parent.joinpath(file).read_text().splitlines())


def test_start_pos():
    array = ARRAYS[0]
    start_pos = [(i, l.find("S")) for i, l in enumerate(array) if l.find("S") > -1]
    assert start_pos == [(1, 1)]

    assert array[1][1] == "S"

    array = ARRAYS[1]
    start_pos = [(i, l.find("S")) for i, l in enumerate(array) if l.find("S") > -1]
    assert start_pos == [(2, 0)]

    assert array[2][0] == "S"


def test_part_one():
    assert part_one(ARRAYS[0]) == 4
    assert part_one(ARRAYS[1]) == 8


def test_part_two():
    assert part_two(ARRAYS[2]) == 4
    assert part_two(ARRAYS[3]) == 8
    assert part_two(ARRAYS[4]) == 10


if __name__ == "__main__":
    test_part_one()
