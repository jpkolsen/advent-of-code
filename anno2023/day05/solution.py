from dataclasses import Field, dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple

INPUT_FILE = Path(__file__).parent.joinpath('input.txt')

@dataclass
class MapRange:
    source_start: int
    dest_start: int
    range_length: int

    def __contains__(self, number: int) -> bool:
        return True if number in range(self.source_start, self.source_start + self.range_length) else False

    def convert(self, number:int) -> int:
        if number in self:
            return self.dest_start + (number - self.source_start)
        return number

@dataclass
class Map:
    title: Optional[str] = ""
    ranges: List[MapRange] = field(default_factory=list)

    def convert(self, source: int) -> int:
        for map_range in self.ranges:
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
                range_map.ranges.append(MapRange(source_start, dest_start, range_length))
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
    return 0

if __name__ == '__main__':
    print('Part one:', part_one(INPUT_FILE))
    print('Part two:', part_two(INPUT_FILE))
