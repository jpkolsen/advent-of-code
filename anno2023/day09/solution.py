from pathlib import Path
from typing import List

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


class History:
    def __init__(self):
        self.layers = []

    def find_diffs(self, sequence: List[int]) -> List[int]:
        diffs = []
        for i in range(len(sequence) - 1):
            diffs.append(sequence[i + 1] - sequence[i])
        return diffs

    def compute_layers(self, sequence: List[int]):
        while not all(seq == sequence[0] for seq in sequence):
            self.layers.append(sequence)
            diffs = self.find_diffs(sequence)
            sequence = self.compute_layers(diffs)
        return sequence

    def propagate_increase(self, sequence: List[int]):
        for layer in self.layers[::-1]:
            sequence.append(sequence[-1] + layer[-1])
        return sequence[-1]


def part_one(lines: list[str]) -> int:
    results = []
    for line in lines:
        sequence = [int(x) for x in line.split()]
        history = History()
        sequence = history.compute_layers(sequence)
        results.append(history.propagate_increase(sequence))

    return sum(results)


def part_two(lines: list[str]) -> int:
    return 0


if __name__ == "__main__":
    print("Part one:", part_one(LINES))
    print("Part two:", part_two(LINES))
