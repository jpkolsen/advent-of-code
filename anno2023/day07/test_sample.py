from pathlib import Path
import random

from .solution import Hand, HandType, part_one, part_two, rank_hands

LINES = Path(__file__).parent.joinpath("sample_input.txt").read_text().splitlines()


def test_hand_types():
    assert Hand("AAAAA", 1).find_type().value == HandType.FIVE_OF_A_KIND.value == 1
    assert Hand("AAAA2", 1).find_type().value == HandType.FOUR_OF_A_KIND.value == 2
    assert Hand("AAABB", 1).find_type().value == HandType.FULL_HOUSE.value == 3
    assert Hand("AAABC", 1).find_type().value == HandType.THREE_OF_A_KIND.value == 4
    assert Hand("AABBC", 1).find_type().value == HandType.TWO_PAIRS.value == 5
    assert Hand("AABCD", 1).find_type().value == HandType.ONE_PAIR.value == 6
    assert Hand("ABCDE", 1).find_type().value == HandType.HIGH_CARD.value == 7


def test_ranked_hands():
    hands = [
        Hand("AAAAA", 1),
        Hand("AAAA2", 1),
        Hand("AAABB", 1),
        Hand("AAABC", 1),
        Hand("AABBC", 1),
        Hand("AABCD", 1),
        Hand("ABCDE", 1),
    ]
    rand = random.Random()
    print(f"Shuffling hands with seed {rand.seed()}")
    shuffled_hands = rand.sample(hands, k=len(hands))

    assert shuffled_hands != hands
    assert rank_hands(shuffled_hands) == hands


def test_part_one():
    assert part_one(LINES) == 6440


def test_part_two():
    assert part_two(LINES) == 0
