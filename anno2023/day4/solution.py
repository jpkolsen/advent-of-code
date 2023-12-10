from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


@dataclass
class Card:
    index: int
    winning_numbers: list[int]
    own_numbers: list[int]

    @property
    def matches(self) -> int:
        return len(set(self.winning_numbers) & set(self.own_numbers))

    @property
    def score(self) -> int:
        return 2 ** (self.matches - 1) if self.matches else 0


def parse_card(line: str) -> Card:
    card_no, results = line.split(":")
    card = Card(
        index=int(card_no.lstrip("Card ")),
        winning_numbers=[int(x) for x in results.split("|")[0].strip().split(" ") if x],
        own_numbers=[int(x) for x in results.split("|")[1].strip().split(" ") if x],
    )
    return card


def part_one(lines: list[str]) -> int:
    cards = [parse_card(line) for line in lines]
    return sum([card.score for card in cards])


def part_two(lines: list[str]) -> int:
    entries = tuple({"copies": 1} for _ in lines)
    for i, line in enumerate(lines):
        card = parse_card(line)
        if card.matches == 0:
            continue
        for entry in entries[i + 1 : i + card.matches + 1]:
            try:
                entry["copies"] += entries[i]["copies"]
            except KeyError:
                pass
    return sum([entry["copies"] for entry in entries])


if __name__ == "__main__":
    print("Part one:", part_one(LINES))
    print("Part two:", part_two(LINES))
