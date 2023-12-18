from enum import Enum, StrEnum, auto
from pathlib import Path
from typing import Optional

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


class HandType(Enum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIRS = auto()
    THREE_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    FIVE_OF_A_KIND = auto()


class Hand:
    def __init__(self, cards: str, bid: int, card_rank: str = "23456789TJQKA"):
        self.cards: str = cards
        self.bid: int = bid
        self.card_rank: str = card_rank
        self._hand_type: HandType = self.find_type()

    @property
    def hand_type(self):
        return self._hand_type

    @hand_type.setter
    def hand_type(self, value: HandType):
        self._hand_type = value

    def __repr__(self):
        return f"{self.cards} ({self.find_type()}) {self.bid}"

    def __lt__(self, other: "Hand"):
        if self.hand_type.value == other.hand_type.value:
            for c_self, c_other in zip(self.cards, other.cards):
                if c_self != c_other:
                    return self.card_rank.index(c_self) < self.card_rank.index(c_other)
        return self.hand_type.value < other.hand_type.value

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

    def optimize_hand(self, cards: str):
        for card in cards:
            if card == "J":
                other_cards = set(cards.replace(card, ""))
                for new_card in other_cards:
                    temp_hand = Hand(cards.replace(card, new_card), 1)
                    if self.hand_type.value < temp_hand.hand_type.value:
                        self.hand_type = temp_hand.hand_type
                    temp_hand.optimize_hand(cards.replace(card, new_card))


def rank_hands(hands: list[Hand]) -> list[Hand]:
    sorted_hands = sorted(hands)
    return sorted_hands


def part_one(lines: list[str]) -> int:
    hands = [Hand(line.split()[0], int(line.split()[1])) for line in lines]
    ranked_hands = rank_hands(hands)
    return sum(i * hand.bid for i, hand in enumerate(ranked_hands, start=1))


def part_two(lines: list[str]) -> int:
    hands = [
        Hand(line.split()[0], int(line.split()[1]), "J23456789TQKA") for line in lines
    ]
    for hand in hands:
        hand.optimize_hand(hand.cards)
    # _ = [hand.optimize_hand(hand.cards) for hand in hands]
    ranked_hands = rank_hands(hands)
    return sum(i * hand.bid for i, hand in enumerate(ranked_hands, start=1))


if __name__ == "__main__":
    print("Part one:", part_one(LINES))
    print("Part two:", part_two(LINES))
