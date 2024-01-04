from pathlib import Path
from typing import List

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


class History:
    def __init__(self):
        self.layers: List[List[int]] = []

    def __str__(self) -> str:
        return "\n".join(
            [(" ".join([str(x) for x in layer])).center(25) for layer in self.layers]
        )

    def find_diffs(self, sequence: List[int]) -> List[int]:
        diffs = []
        for i in range(len(sequence) - 1):
            diffs.append(sequence[i + 1] - sequence[i])
        return diffs

    def compute_layers(self, sequence: List[int]):
        """
        Compute 'layers' of differences.

        While all elements are the not the same, compute the difference between each.
        Add a 'layer', i.e. a list of all the differences and process that recursively.
        """
        while not all(seq == sequence[0] for seq in sequence):
            self.layers.append(sequence)
            diffs = self.find_diffs(sequence)
            sequence = self.compute_layers(diffs)
        return sequence

    def propagate_increase(self, difference: int, forward: bool = True):
        """Apend an entry to all layers by adding the final entry of the previous layer to the final entry of the current one"""
        extrapolations = [difference]
        for layer in self.layers[::-1]:
            value = (
                layer[-1] + extrapolations[-1]
                if forward
                else layer[0] - extrapolations[-1]
            )
            extrapolations.append(value)
        return extrapolations[-1]


def part_one(lines: list[str]) -> int:
    results = []
    for line in lines:
        sequence = [int(x) for x in line.split()]
        history = History()
        sequence = history.compute_layers(sequence)
        results.append(history.propagate_increase(sequence[0]))
    return sum(results)


def part_two(lines: list[str]) -> int:
    results = []
    for line in lines:
        sequence = [int(x) for x in line.split()]
        history = History()
        sequence = history.compute_layers(sequence)
        results.append(history.propagate_increase(sequence[0], forward=False))
    return sum(results)


if __name__ == "__main__":
    print("Part one:", part_one(LINES))
    print("Part two:", part_two(LINES))
