from pathlib import Path
from typing import List

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


def parse_file(lines: List[str]):
    elements = {}
    steps = lines[0]
    for line in lines[2:]:
        location, directions = line.split(" = ")
        elements[location.strip()] = directions.strip("(").strip(")").split(", ")
    return steps, elements


def part_one(lines: List[str]):
    steps, elements = parse_file(lines)
    location = "AAA"
    counter = 0
    while not location == "ZZZ":
        for step in steps:
            location = elements[location][0] if step == "L" else elements[location][1]
            counter += 1
    return counter


def part_two(input_file) -> int:
    return 0


if __name__ == "__main__":
    print("Part one:", part_one(LINES))
    print("Part two:", part_two(LINES))
