from dataclasses import Field, dataclass, field
from enum import StrEnum, auto
from itertools import cycle
from pathlib import Path
from typing import Callable, List, Optional, Set, Tuple

import numpy as np

INPUT_FILE = Path(__file__).parent.joinpath('input.txt')

@dataclass
class RangeMap:
    source_start: int
    dest_start: int
    range_length: int

    @property
    def source_end(self) -> int:
        return self.source_start + self.range_length

    @property
    def source_array(self) -> np.ndarray:
        return np.array(range(self.source_start, self.source_end))

    @property
    def conversion(self) -> int:
        return self.dest_start - self.source_start

    def __contains__(self, number: int) -> bool:
        return True if number in range(self.source_start, self.source_end) else False

    def convert(self, number:int) -> int:
        if number in self:
            return self.dest_start + (number - self.source_start)
        return number

    def convert_array(self, array: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        # Values not in self.source_array are not converted
        not_converted = np.setdiff1d(array, self.source_array)

        # Values
        converted = np.intersect1d(array, self.source_array) + self.conversion

        return not_converted, converted


@dataclass
class Map:
    title: Optional[str] = ""
    range_maps: List[RangeMap] = field(default_factory=list)

    def convert(self, source: int) -> int:
        for map_range in self.range_maps:
            if source in map_range:
                return map_range.convert(source)
        return source

    def convert_array(self, array: np.ndarray) -> np.ndarray:
        out_array = np.array([], dtype="int")
        for range_map in self.range_maps:
            array, converted = range_map.convert_array(array)
            out_array = np.union1d(out_array, converted)
        return np.union1d(out_array, array)


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
                range_map.range_maps.append(RangeMap(source_start, dest_start, range_length))
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

def get_seed_array(values: List[int]) -> np.ndarray:
    start = 0

    seeds = np.array(range(0,0))
    for i, value in enumerate(values):
        if not i%2:
            start = value
        else:
            end = start + value
            seeds = np.hstack((seeds, np.array(range(start, end))))
    return seeds

def part_two(input_file: Path) -> int:
    seed_ranges, maps = parse_input(input_file)
    
    min_value = 9999999999999999999
    start = 0
    for i, value in enumerate(seed_ranges):
        if not i%2:
            start = value
        else:
            end = start + value
            seeds = range(start, end)
            for seed in seeds:
                location = convert_multiple_maps(seed, maps)
                if location < min_value:
                    min_value = location
            
    return min_value

def part_two_numpy(input_file: Path) -> int:
    seed_ranges, maps = parse_input(input_file)
    
    array = get_seed_array(seed_ranges)
    print(array)
    for conversion_map in maps:
        print(f"Processing {conversion_map.title}")
        array = conversion_map.convert_array(array)
    return np.min(array)

if __name__ == '__main__':
    print('Part one:', part_one(INPUT_FILE))
    print('Part two:', part_two_numpy(INPUT_FILE))
