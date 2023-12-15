from dataclasses import dataclass
import math
from pathlib import Path
from typing import List, Tuple

import numpy as np

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


@dataclass
class Race:
    time: int
    distance: int

    @property
    def discriminant(self):
        return self.time**2 - 4 * self.distance

    @property
    def beat_times(self):
        low = math.ceil((self.time - math.sqrt(self.discriminant)) / 2)
        high = math.floor((self.time + math.sqrt(self.discriminant)) / 2)
        low = low if not low * (self.time - low) == self.distance else low + 1
        high = high if not high * (self.time - high) == self.distance else high - 1
        return low, high

    @property
    def num_solutions(self):
        return self.beat_times[1] - self.beat_times[0] + 1


def parse_races(lines: List[str]) -> Tuple:
    lines = [line.split(":")[1] for line in lines]
    times = [int(val) for val in lines[0].split()]
    distances = [int(val) for val in lines[1].split()]
    return times, distances


def part_one(lines: list[str]) -> int:
    races = [Race(time, distance) for time, distance in zip(*parse_races(lines))]
    _ = [print(race.beat_times) for race in races]
    solutions = [race.num_solutions for race in races]
    print(solutions)
    return np.prod(solutions)


def part_two(lines: list[str]) -> int:
    times, distances = parse_races(lines)
    time = int("".join(str(val) for val in times))
    distance = int("".join(str(val) for val in distances))
    race = Race(time, distance)
    return race.num_solutions


if __name__ == "__main__":
    print("Part one:", part_one(LINES))
    print("Part two:", part_two(LINES))
