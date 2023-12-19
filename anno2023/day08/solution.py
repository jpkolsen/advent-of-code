from pathlib import Path
from typing import Dict, List, Tuple

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


def parse_lines(lines: List[str]) -> Tuple[List[str], Dict[str, List[str]]]:
    elements = {}
    steps = lines[0]
    for line in lines[2:]:
        location, directions = line.split(" = ")
        elements[location.strip()] = directions.strip("(").strip(")").split(", ")
    return steps, elements


def part_one(lines: List[str]):
    steps, elements = parse_lines(lines)
    location = "AAA"
    counter = 0
    while not location == "ZZZ":
        for step in steps:
            location = elements[location][0] if step == "L" else elements[location][1]
            counter += 1
    return counter


def part_two(lines: List[str]) -> int:
    steps, elements = parse_lines(lines)
    locations = [x for x in elements.keys() if x.endswith("A")]

    num_locations = len(locations)
    counter = 1
    while True:
        for step in steps:
            locations = [
                elements[location][0] if step == "L" else elements[location][1]
                for location in locations
            ]
            if any(location == "XXX" for location in locations):
                raise ValueError("XXX")
            if all(location.endswith("Z") for location in locations):
                return counter
            counter += 1


if __name__ == "__main__":
    print("Part one:", part_one(LINES))
    print("Part two:", part_two(LINES))
