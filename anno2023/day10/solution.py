from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import StrEnum, auto
from pathlib import Path
from typing import Callable, List, Tuple

ARRAY = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


class InvalidDirectionError(Exception):
    ...


class Direction(StrEnum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


@dataclass
class Position:
    x: int
    y: int


Tile = Callable[[Direction], Direction]


def north_south(direction: Direction) -> Direction:
    if direction == Direction.NORTH:
        return Direction.NORTH
    elif direction == Direction.SOUTH:
        return Direction.SOUTH
    else:
        raise ValueError("Invalid direction")


def east_west(direction: Direction) -> Direction:
    if direction == Direction.EAST:
        return Direction.EAST
    elif direction == Direction.WEST:
        return Direction.WEST
    else:
        raise ValueError("Invalid direction")


def north_east(direction: Direction) -> Direction:
    if direction == Direction.SOUTH:
        return Direction.EAST
    elif direction == Direction.WEST:
        return Direction.NORTH
    else:
        raise ValueError("Invalid direction")


def north_west(direction: Direction) -> Direction:
    if direction == Direction.SOUTH:
        return Direction.WEST
    elif direction == Direction.EAST:
        return Direction.NORTH
    else:
        raise ValueError("Invalid direction")


def south_west(direction: Direction) -> Direction:
    if direction == Direction.NORTH:
        return Direction.WEST
    elif direction == Direction.EAST:
        return Direction.SOUTH
    else:
        raise ValueError("Invalid direction")


def south_east(direction: Direction) -> Direction:
    if direction == Direction.NORTH:
        return Direction.EAST
    elif direction == Direction.WEST:
        return Direction.SOUTH
    else:
        raise ValueError("Invalid direction")


def start_end(direction: Direction) -> Direction:
    raise InvalidDirectionError("No direction found")


tiles = {
    "|": north_south,
    "-": east_west,
    "L": north_east,
    "J": north_west,
    "7": south_west,
    "F": south_east,
    "S": start_end,
}


def move(position: Position, direction: Direction) -> Position:
    if direction == Direction.NORTH:
        return Position(position.x, position.y - 1)
    elif direction == Direction.SOUTH:
        return Position(position.x, position.y + 1)
    elif direction == Direction.EAST:
        return Position(position.x + 1, position.y)
    elif direction == Direction.WEST:
        return Position(position.x - 1, position.y)
    else:
        raise ValueError("Invalid direction")


def step_forward(
    array: List[str], position: Position, direction: Direction
) -> Tuple[Position, Direction]:
    tile = tiles[array[position.y][position.x]]
    new_direction = tile(direction)
    new_position = move(position, new_direction)
    return new_position, new_direction


def part_one(array: List[str]) -> int:
    start_pos_coordinates = [
        (i, l.find("S")) for i, l in enumerate(array) if l.find("S") > -1
    ][0]
    start_position = Position(start_pos_coordinates[1], start_pos_coordinates[0])
    direction = None
    while direction is None:
        if array[start_position.y - 1][start_position.x] in ["|", "7", "F"]:
            # north tile connects
            position = Position(start_position.x, start_position.y - 1)
            direction = Direction.NORTH
        elif array[start_position.y + 1][start_position.x] in ["|", "J", "L"]:
            # south tile connects
            position = Position(start_position.x, start_position.y + 1)
            direction = Direction.SOUTH
        elif array[start_position.y][start_position.x + 1] in ["-", "J", "7"]:
            # east tile connects
            position = Position(start_position.x + 1, start_position.y)
            direction = Direction.EAST
        elif array[start_position.y][start_position.x - 1] in ["-", "L", "F"]:
            # west tile connects
            position = Position(start_position.x - 1, start_position.y)
            direction = Direction.WEST
        else:
            raise InvalidDirectionError("No direction found")

    steps = 1
    while True:
        try:
            position, direction = step_forward(array, position, direction)
            steps += 1
        except InvalidDirectionError:
            break
    return steps / 2


def part_two(array: List[List[str]]) -> int:
    return 0


if __name__ == "__main__":
    print("Part one:", part_one(ARRAY))
    print("Part two:", part_two(ARRAY))
