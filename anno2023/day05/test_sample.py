from pathlib import Path

import numpy as np
import pytest

from anno2023.day05.solution import (Map, MapRange, convert_multiple_maps,
                                     parse_input, part_one, part_two,
                                     split_range_by_overlap)

INPUT_FILE = Path(__file__).parent.joinpath("sample_input.txt")


def test_map_range():
    map_range = MapRange(source_start=0, dest_start=5, range_length=10)
    assert 0 in map_range
    assert 9 in map_range
    assert 10 not in map_range


def test_convert():
    map_range = MapRange(source_start=5, dest_start=10, range_length=2)
    assert map_range.convert(3) == 3
    assert map_range.convert(5) == 10
    assert map_range.convert(6) == 11
    assert map_range.convert(7) == 7


def test_convert_negative():
    map_range = MapRange(source_start=5, dest_start=2, range_length=10)
    assert map_range.convert(2) == 2
    assert map_range.convert(5) == 2
    assert map_range.convert(10) == 7
    assert map_range.convert(15) == 15


@pytest.mark.parametrize(
    "source, dest",
    [(0, 5), (1, 6), (2, 2), (9, 9), (10, 15), (11, 16), (12, 22), (21, 31), (22, 22)],
)
def test_map_convert(source: int, dest: int):
    _map = Map(
        map_ranges=[MapRange(0, 5, 2), MapRange(10, 15, 2), MapRange(12, 22, 10)]
    )
    assert _map.convert(source) == dest


@pytest.mark.parametrize("source, dest", [(0, 5), (5, 15), (6, 16), (9, 14)])
def test_multiple_maps_convert(source: int, dest: int):
    maps = [Map(map_ranges=[MapRange(0, 5, 10)]), Map(map_ranges=[MapRange(10, 15, 2)])]
    assert convert_multiple_maps(source, maps) == dest


# def test_get_seed_array():
#     values = [5, 2, 10, 3]
#     assert all(get_seed_array(values) == np.array([5, 6, 10, 11, 12]))
 

# def test_convert_array():
#     from anno2023.day05.numpy_solution import RangeMap

#     range_map = RangeMap(5, 10, 2)
#     array = np.array(range(4, 8), dtype="int")
#     assert all(np.union1d(*range_map.convert_array(array)) == np.array([4, 7, 10, 11]))

#     array = np.array(range(4, 13))
#     assert all(
#         np.union1d(*range_map.convert_array(array))
#         == np.array([4, 7, 8, 9, 10, 11, 12])
#     )
 
 
# def test_convert_multiple_range_array():
#     from anno2023.day05.numpy_solution import Map, RangeMap

#     maps = Map(range_maps=[RangeMap(5, 10, 2), RangeMap(15, 20, 2)])
#     array = np.array(range(4, 16))
#     assert all(
#         maps.convert_array(array) == np.array([4, 7, 8, 9, 10, 11, 12, 13, 14, 20])
#     )

def test_get_overlap():
    # Overlap in middle
    range1 = range(0,10)
    range2 = range(4,6)
    assert [(r.start, r.stop) for r in (range(0,4), range(4,6), range(6, 10))] == [(r.start, r.stop) for r in split_range_by_overlap(range1, range2)]

    # Overlap at upper end
    range1 = range(0, 6)
    range2 = range(4, 10)
    assert [(r.start, r.stop) for r in (range(0,4), range(4,6), range(0, 0))] == [(r.start, r.stop) for r in split_range_by_overlap(range1, range2)]

    # No overlap (lower)
    range1 = range(0,4)
    range2 = range(6, 10)
    assert [(r.start, r.stop) for r in (range(0,4), range(0,0), range(0, 0))] == [(r.start, r.stop) for r in split_range_by_overlap(range1, range2)]

    # No overlap (over)
    range1 = range(6, 10)
    range2 = range(0, 6)
    assert [(r.start, r.stop) for r in (range(0,0), range(0,0), range(6, 10))] == [(r.start, r.stop) for r in split_range_by_overlap(range1, range2)]

    # Overlap at lower end
    range1 = range(4, 10)
    range2 = range(0, 6)
    assert [(r.start, r.stop) for r in (range(0,0), range(4,6), range(6, 10))] == [(r.start, r.stop) for r in split_range_by_overlap(range1, range2)]

    # Full overlap
    range1 = range(4, 6)
    range2 = range(0, 10)
    assert [(r.start, r.stop) for r in (range(0,0), range(4,6), range(0, 0))] == [(r.start, r.stop) for r in split_range_by_overlap(range1, range2)]

def test_convert_range():
    map_range = MapRange(source_start=4, dest_start=6, range_length=10)
    assert map_range.convert_range(range(4, 6)) == range(6, 8)

    with pytest.raises(ValueError):
        map_range.convert_range(range(0, 10))

    with pytest.raises(ValueError):
        map_range.convert_range(range(4, 15))


def test_part_one():
    assert part_one(input_file=INPUT_FILE) == 35


def test_part_two():
    assert part_two(INPUT_FILE) == 46


if __name__ == "__main__":
    import time

    start_time = time.time()
    print(part_two(INPUT_FILE))
    print(f"Executed in {(time.time() - start_time)*1000} ms")
