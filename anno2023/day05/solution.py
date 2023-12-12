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
    def end(self) -> int:
        return self.start + self.length

    @property
    def index_range(self):
        return range(self.start, self.end)


@dataclass
class MapRange:
    source_start: int
    dest_start: int
    range_length: int

    @property
    def source_end(self) -> int:
        return self.source_start + self.range_length

    @property
    def conversion(self) -> int:
        return self.dest_start - self.source_start

    def __contains__(self, number: int) -> bool:
        return True if number in range(self.source_start, self.source_end) else False

    def convert(self, number: int) -> int:
        if number in self:
            return self.dest_start + (number - self.source_start)
        return number


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


def part_one(input_file: Path) -> int:
    seeds, maps = parse_input(input_file)
    locations = []
    for seed in seeds:
        locations.append(convert_multiple_maps(seed, maps))
    return min(locations)


def part_two(input_file: Path) -> int:
    seed_input, maps = parse_input(input_file)

    seed_ranges = [
        PropertyRange(start=seed_input[i - 1], length=seed_input[i])
        for i, _ in enumerate(seed_input[1:])
    ]
    for conversion_map in maps:
        pass


if __name__ == "__main__":
    print("Part one:", part_one(INPUT_FILE))
    print("Part two:", part_two(INPUT_FILE))
