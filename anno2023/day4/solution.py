from pathlib import Path

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


def part_one(lines: list[str]) -> int:
    pass


def part_two(lines: list[str]) -> int:
    pass


if __name__ == "__main__":
    print(part_one(LINES))
