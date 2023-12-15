from dataclasses import Field, dataclass, field
from enum import StrEnum, auto
from itertools import cycle
from pathlib import Path
from typing import Callable, List, Optional, Set, Tuple

import numpy as np

INPUT_FILE = Path(__file__).parent.joinpath("input.txt")


@dataclass
class MapRange:
    source_start: int
    dest_start: int
    range_length: int

    @property
    def source_end(self) -> int:
        return self.source_start + self.range_length

    @property
    def as_range(self) -> range:
        return range(self.source_start, self.source_end)

    def __contains__(self, number: int) -> bool:
        return True if number in range(self.source_start, self.source_end) else False

    def convert(self, number: int) -> int:
        if number in self:
            return self.dest_start + (number - self.source_start)
        return number

    def convert_range(self, range_in: range) -> range:
        if not (range_in.start in self and range_in.stop - 1 in self):
            raise ValueError
        return range(self.convert(range_in.start), self.convert(range_in.stop))


@dataclass
class Map:
    title: Optional[str] = ""
    map_ranges: List[MapRange] = field(default_factory=list)

    def convert(self, source: int) -> int:
        for map_range in self.map_ranges:
            if source in map_range:
                return map_range.convert(source)
        return source


def parse_input(input_file: Path) -> Tuple[List[int], List[Map]]:
    with open(input_file) as f:
        seeds = [int(x) for x in f.readline().split(":")[1].split()]
        _ = f.readline()  # skip blank row

        maps = []
        range_map = Map()
        for line in f.read().splitlines():
            if not line:
                maps.append(range_map)
            elif line.endswith(":"):
                range_map = Map(title=line.strip(":"))
            else:
                dest_start, source_start, range_length = (int(x) for x in line.split())
                range_map.map_ranges.append(
                    MapRange(source_start, dest_start, range_length)
                )
        maps.append(range_map)
    return (seeds, maps)


def convert_multiple_maps(source: int, maps: List[Map]) -> int:
    number = source
    for _map in maps:
        number = _map.convert(number)
    return number


def split_range_by_overlap(range1: range, range2: range):
    """Divide range1 into sub-ranges by their overlap with range2"""
    range1_below = (
        range(range1.start, min(range2.start, range1.stop))
        if range1.start < range2.start
        else range(0, 0)
    )
    overlap = range(max(range1.start, range2.start), min(range1.stop, range2.stop))
    overlap = range(0, 0) if not overlap else overlap
    range1_above = (
        range(max(range2.stop, range1.start), range1.stop)
        if range2.stop < range1.stop
        else range(0, 0)
    )
    return overlap, (range1_below, range1_above)


def part_one(input_file: Path) -> int:
    seeds, maps = parse_input(input_file)
    locations = []
    for seed in seeds:
        locations.append(convert_multiple_maps(seed, maps))
    return min(locations)


class Convertor:
    def __init__(self, maps: List[Map]):
        self.maps = maps
        self.lowest_value = np.inf

    def convert_range(self, _range: range, maps: List[Map]) -> None:
        while maps:
            _map = maps.pop()

            for map_range in _map.map_ranges:
                overlap, non_overlap = split_range_by_overlap(
                    _range, map_range.as_range
                )
                if overlap:
                    self.convert_range(map_range.convert_range(overlap), maps)
                    if not any(non_overlap):
                        return
                    _range = non_overlap[0]
                    if all(non_overlap):
                        self.convert_range(non_overlap[1], maps)

            self.convert_range(_range, maps)
        self.lowest_value = min(self.lowest_value, _range.start)
        print(self.lowest_value)


def part_two(input_file: Path) -> int:
    seed_input, maps = parse_input(input_file)

    ranges = []
    for i, value in enumerate(seed_input):
        if not i % 2:
            start = value
        else:
            ranges.append(range(start, value + 1))

    import time

    convertor = Convertor(maps)
    for _range in ranges:
        convertor.convert_range(_range, maps.copy())
    return convertor.lowest_value


if __name__ == "__main__":
    print("Part one:", part_one(INPUT_FILE))
    print("Part two:", part_two(INPUT_FILE))
