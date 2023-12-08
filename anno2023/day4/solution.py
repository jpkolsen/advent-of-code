from dataclasses import dataclass
from pathlib import Path

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


@dataclass
class Card:
    index: int
    winning_numbers: list[int]
    own_numbers: list[int]

    @property
    def score(self) -> int:
        if len(set(self.winning_numbers) & set(self.own_numbers)) == 0:
            return 0
        return 2 ** (len(set(self.winning_numbers) & set(self.own_numbers)) - 1)


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
    pass


if __name__ == "__main__":
    print(part_one(LINES))
