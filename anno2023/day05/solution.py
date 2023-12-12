from dataclasses import Field, dataclass, field
from enum import StrEnum, auto
from itertools import cycle
from pathlib import Path
from typing import Callable, List, Optional, Set, Tuple

import numpy as np

INPUT_FILE = Path(__file__).parent.joinpath("input.txt")


@dataclass
class PropertyRange:
    start: int
    length: int

    @property
    def stop(self) -> int:
        return self.start + self.length

    @property
    def as_range(self):
        return range(self.start, self.stop)


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
        if not (range_in.start in self and range_in.stop in self):
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
    
    def coerce_ranges(self, ranges: List[PropertyRange]) -> List[PropertyRange]:
        pass

    def convert_ranges(self, ranges: List[PropertyRange]) -> List[PropertyRange]:
        converted_ranges = []
        for _range in ranges:
            converted_ranges.append(
                PropertyRange(start=self.convert(_range.start), length=_range.length)
            )
        return converted_ranges


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
    range1_below = range(range1.start, min(range2.start, range1.stop)) if range1.start < range2.start else range(0,0)
    overlap = range(max(range1.start, range2.start), min(range1.stop, range2.stop))
    overlap = range(0,0) if not overlap else overlap
    range1_above = range(max(range2.stop, range1.start), range1.stop) if range2.stop < range1.stop else range(0,0)
    return range1_below, overlap, range1_above


def part_one(input_file: Path) -> int:
    seeds, maps = parse_input(input_file)
    locations = []
    for seed in seeds:
        locations.append(convert_multiple_maps(seed, maps))
    return min(locations)


def part_two(input_file: Path) -> int:
    seed_input, maps = parse_input(input_file)

    ranges_in = []
    for i, value in enumerate(seed_input):
        if not i%2:
            start = value
        else:
            ranges_in.append(PropertyRange(start=start, length=value))

    ranges_out = []
    for conversion_map in maps:
        for map_range in conversion_map.map_ranges:
            for prop_range in ranges_in:
                below, overlap, above = split_range_by_overlap(range(prop_range.start, prop_range.stop), map_range.as_range)
                overlap = map_range.convert_range(overlap) if overlap else overlap
                ranges_out.extend([_range for _range in (below, overlap, above) if _range])
        ranges_in = ranges_out
        ranges_out = []
    return min(r.start for r in ranges_out)

if __name__ == "__main__":
    print("Part one:", part_one(INPUT_FILE))
    print("Part two:", part_two(INPUT_FILE))
