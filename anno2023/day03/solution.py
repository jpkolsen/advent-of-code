import re
from pathlib import Path

LINES = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
SYMBOLS = {"\\" + c for c in "".join(LINES) if not c.isdigit() and c != "."}
SYMBOLS_REGEX = r"|".join(SYMBOLS)
NUMBER_REGEX = r"\d+"


def find_symbols(line: str, regex: str) -> set[re.Match]:
    return {m for m in re.finditer(regex, line)}


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
            symbol_match.start()
            for l in [prev_line, curr_line, next_line]
            for symbol_match in find_symbols(l, SYMBOLS_REGEX)
        }

        # Find all numbers in the current line that are adjacent to a symbol
        for number_match in re.finditer(NUMBER_REGEX, curr_line):
            if any(
                i in indexes
                for i in range(number_match.start() - 1, number_match.end() + 1)
            ):
                part_numbers.append(int(number_match.group()))

        # Iterate lines
        prev_line = curr_line
        curr_line = next_line
    return sum(part_numbers)


def part_two(lines: list[str]) -> int:
    curr_line = ""
    prev_line = ""

    part_numbers = []
    for line in lines + [""]:
        next_line = line
        if not curr_line:
            curr_line = next_line
            continue

        # Find all indexes of * symbols in the current line
        indexes = {m.start() for m in find_symbols(curr_line, r"\*")}

        # Find all numbers adjacet to a * symbol
        for index in indexes:
            gears = []
            number_matches = {
                number_match
                for l in [prev_line, curr_line, next_line]
                for number_match in find_symbols(l, NUMBER_REGEX)
            }
            for match in number_matches:
                if index in range(match.start() - 1, match.end() + 1):
                    gears.append(int(match.group()))
            if len(gears) == 2:
                part_numbers.append(gears[0] * gears[1])

        # Iterate lines
        prev_line = curr_line
        curr_line = next_line
    return sum(part_numbers)


if __name__ == "__main__":
    print(part_two(LINES))
