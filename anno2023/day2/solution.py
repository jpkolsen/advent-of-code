from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np

lines = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


@dataclass
class Round:
    red: Optional[int] = 0
    blue: Optional[int] = 0
    green: Optional[int] = 0

    def parse_result(self, round: str):
        results = [x for x in round.split(",")]
        for result in results:
            count, color = result.strip().split(" ")
            setattr(self, color.lower(), int(count))
        return self

    def __gt__(self, other):
        return (
            self.red > other.red or self.blue > other.blue or self.green > other.green
        )

    def __lt__(self, other):
        return (
            self.red < other.red or self.blue < other.blue or self.green < other.green
        )


@dataclass
class Game:
    index: int
    rounds: list[Round]

    @property
    def power(self):
        max_cubes = {}
        for color in ["red", "blue", "green"]:
            max_cubes[color] = max([getattr(round, color) for round in self.rounds])
        return np.prod(list(max_cubes.values()))


def parse_games(lines: str) -> list[Game]:
    all_games = []
    for line in lines:
        game_no, results = line.split(":")
        rounds = results.split(";")
        game = Game(
            index=int(game_no.lstrip("Game ")),
            rounds=[Round().parse_result(round) for round in rounds],
        )
        all_games.append(game)
    return all_games


def part_one(all_games: list[Game]) -> int:
    max_round = Round(red=12, blue=14, green=13)

    possible_games = []
    for game in all_games:
        if not any([round > max_round for round in game.rounds]):
            possible_games.append(game)
    return sum([game.index for game in possible_games])


def part_two(all_games: list[Game]):
    power = 0
    for game in all_games:
        power += game.power
    return power


if __name__ == "__main__":
    all_games = parse_games(lines)
    print(part_two(all_games))
