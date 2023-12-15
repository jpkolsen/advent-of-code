from enum import Enum, StrEnum, auto
from pathlib import Path

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


class HandType(Enum):
    FIVE_OF_A_KIND = auto()
    FOUR_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    THREE_OF_A_KIND = auto()
    TWO_PAIRS = auto()
    ONE_PAIR = auto()
    HIGH_CARD = auto()


class Hand:
    card_rank = list("23456789TJQKA")

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid

    def __repr__(self):
        return self.find_type().value

    def __lt__(self, other: "Hand"):
        return self.find_type().value < other.find_type().value

    def find_type(self) -> HandType:
        if self.cards.count(self.cards[0]) == 5:
            return HandType.FIVE_OF_A_KIND
        elif any(self.cards.count(c) == 4 for c in self.cards):
            return HandType.FOUR_OF_A_KIND
        elif any(self.cards.count(c) == 3 for c in self.cards):
            if any(self.cards.count(c) == 2 for c in self.cards):
                return HandType.FULL_HOUSE
            else:
                return HandType.THREE_OF_A_KIND
        elif any(self.cards.count(c) == 2 for c in self.cards):
            non_unique = [c for c in self.cards if self.cards.count(c) == 2]
            if len(non_unique) == 4:
                return HandType.TWO_PAIRS
            else:
                return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD


def rank_hands(hands: list[Hand]) -> list[Hand]:
    return sorted(hands)


def part_one(lines: list[str]) -> int:
    hands = [Hand(line.split()[0], int(line.split()[1])) for line in lines]


def part_two(lines: list[str]) -> int:
    return 0


if __name__ == "__main__":
    print("Part one:", part_one(LINES))
    print("Part two:", part_two(LINES))
