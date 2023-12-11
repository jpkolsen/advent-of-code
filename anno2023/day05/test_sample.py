from pathlib import Path

import pytest
from .solution import (Map, MapRange, convert_multiple_maps, part_one,
                            part_two)

INPUT_FILE = Path(__file__).parent.joinpath('sample_input.txt')


def test_map_range():
    map_range = MapRange(source_start=0, dest_start = 5, range_length=10)
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

@pytest.mark.parametrize("source, dest", [(0, 5), (1, 6), (2, 2),(9, 9), (10, 15), (11, 16), (12, 22), (21, 31), (22, 22)])
def test_map_convert(source: int, dest:int):
    _map = Map(ranges=[MapRange(0, 5, 2), MapRange(10, 15, 2), MapRange(12, 22, 10)])
    assert _map.convert(source) == dest

@pytest.mark.parametrize("source, dest", [(0, 5), (5, 15), (6, 16), (9, 14)])
def test_multiple_maps_convert(source: int, dest: int):
    maps = [Map(ranges=[MapRange(0, 5, 10)]), Map(ranges=[MapRange(10, 15, 2)])]
    assert convert_multiple_maps(source, maps) == dest

def test_part_one():
    assert part_one(input_file=INPUT_FILE) == 35


def test_part_two():
    assert part_two(INPUT_FILE) == 0


if __name__=="__main__":
    test_part_one()
