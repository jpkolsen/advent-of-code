from pathlib import Path
import re

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
SYMBOLS = {"\\" + c for c in "".join(LINES) if not c.isdigit() and c != "."}
SYMBOLS_REGEX = r"|".join(SYMBOLS)
NUMBER_REGEX = r"\d+"


def find_symbols(line: str) -> set[int]:
    return {m.start() for m in re.finditer(SYMBOLS_REGEX, line)}


def part_one(lines: list[str]) -> int:
    curr_line = ""
    prev_line = ""

    part_numbers = []
    for line in lines + [""]:
        next_line = line
        if not curr_line:
            curr_line = next_line
            continue

        # Find all indexes of symbols in the current line and the one above and below
        indexes = {
            i for l in [prev_line, curr_line, next_line] for i in find_symbols(l)
        }

        # Find all numbers in the current line that are adjacent to a symbol
        for m in re.finditer(NUMBER_REGEX, curr_line):
            if any(x in indexes for x in range(m.start() - 1, m.end() + 1)):
                part_numbers.append(int(m.group()))

        # Iterate lines
        prev_line = curr_line
        curr_line = next_line
    return sum(part_numbers)


def part_two(lines: list[str]) -> int:
    pass


if __name__ == "__main__":
    print(part_one(LINES))
