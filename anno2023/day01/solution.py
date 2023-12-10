from pathlib import Path

lines = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()

# Part 1
values = []
for line in lines:
    digits = [x for x in line if x.isdigit()]
    values.append(int("".join((digits[0], digits[-1]))))

print(sum(values))

# Part 2
words = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]


def find_first_match(target, words):
    while True:
        matches = [target.startswith(word) for word in words]
        if any(matches):
            first = words[matches.index(True)]
            return first if first.isdigit() else words.index(first) + 1
        target = target[1:]


values = []
for line in lines:
    first = find_first_match(line, words)
    last = find_first_match(line[::-1], [word[::-1] for word in words])
    values.append(int("".join((str(first), str(last)))))

print(sum(values))
