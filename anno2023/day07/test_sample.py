from pathlib import Path
import random

from anno2023.day07.solution import (
    Hand,
    HandType,
    part_one,
    part_two,
    rank_hands,
)

LINES = Path(__file__).parent.joinpath("sample_input.txt").read_text().splitlines()


def test_hand_types():
    assert Hand("AAAAA", 1).find_type().value == HandType.FIVE_OF_A_KIND.value == 7
    assert Hand("AAAA2", 1).find_type().value == HandType.FOUR_OF_A_KIND.value == 6
    assert Hand("AAABB", 1).find_type().value == HandType.FULL_HOUSE.value == 5
    assert Hand("AAABC", 1).find_type().value == HandType.THREE_OF_A_KIND.value == 4
    assert Hand("AABBC", 1).find_type().value == HandType.TWO_PAIRS.value == 3
    assert Hand("AABCD", 1).find_type().value == HandType.ONE_PAIR.value == 2
    assert Hand("ABCDE", 1).find_type().value == HandType.HIGH_CARD.value == 1


def test_compare_hand_types():
    assert Hand("AAAAA", 1) > Hand("AAAA2", 1)
    assert Hand("AAAA2", 1) > Hand("AAABB", 1)
    assert Hand("AAABB", 1) > Hand("AAABC", 1)
    assert Hand("AAABC", 1) > Hand("AABBC", 1)
    assert Hand("AABBC", 1) > Hand("AABCD", 1)
    assert Hand("AABCD", 1) > Hand("ABCDE", 1)


def test_rank_hand_types():
    hands = [
        Hand("AAAAA", 1),
        Hand("AAAA2", 1),
        Hand("AAABB", 1),
        Hand("AAABC", 1),
        Hand("AABBC", 1),
        Hand("AABCD", 1),
        Hand("ABCDE", 1),
    ]
    hands.reverse()
    rand = random.Random()
    print(f"Shuffling hands with seed {rand.seed()}")
    shuffled_hands = rand.sample(hands, k=len(hands))

    assert shuffled_hands != hands
    assert rank_hands(shuffled_hands) == hands


def test_compare_cards():
    assert Hand("AAAAA", 1) > Hand("KKKKK", 1)
    assert Hand("KK677", 1) > Hand("KTJJT", 1)
    assert Hand("QQQJA", 1) > Hand("T55J5", 1)


def test_rank_card_values():
    hands = [Hand(f"{c}{c}{c}{c}{c}", 1) for c in "23456789TJQKA"]
    rand = random.Random()
    print(f"Shuffling hands with seed {rand.seed()}")
    shuffled_hands = rand.sample(hands, k=len(hands))

    assert shuffled_hands != hands
    assert rank_hands(shuffled_hands) == hands

    hands = [
        Hand("T55J5", 1),
        Hand("QQQJA", 1),
    ]
    shuffled_hands = hands.copy()[::-1]
    assert shuffled_hands != hands
    assert rank_hands(shuffled_hands) == hands

    hands = [
        Hand("KTJJT", 1),
        Hand("KK677", 1),
    ]
    shuffled_hands = hands.copy()[::-1]

    assert shuffled_hands != hands
    assert rank_hands(shuffled_hands) == hands


def test_optimize_hand():
    hand = Hand("T55J5", 1)
    assert hand.hand_type == HandType.THREE_OF_A_KIND
    hand.optimize_hand(hand.cards)
    assert hand.hand_type == HandType.FOUR_OF_A_KIND

    hand = Hand("T12J5", 1)
    assert hand.hand_type == HandType.HIGH_CARD
    hand.optimize_hand(hand.cards)
    assert hand.hand_type == HandType.ONE_PAIR


def test_part_one():
    assert part_one(LINES) == 6440


def test_part_two():
    assert part_two(LINES) == 5905


if __name__ == "__main__":
    test_part_two()
