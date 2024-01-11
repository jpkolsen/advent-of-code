from pathlib import Path

LINES = Path(__file__).parent.joinpath('input.txt').read_text().splitlines()

def part_one(lines: list[str]) -> int:
    return 0


def part_two(lines: list[str]) -> int:
    return 0

if __name__ == '__main__':
    print('Part one:', part_one(LINES))
    print('Part two:', part_two(LINES))
