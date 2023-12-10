#!/bin/bash

echo "Attempting to create a directory for the next challenge in the advent of code"

# Check for existing dayXX directories
existing_dirs=(day[0-9][0-9])
if [ ${#existing_dirs[@]} -eq 0 ]; then
    read -p "No previous challenges found. Start with day01? [y/n]: " response
    if [ "$response" != "y" ]; then
        echo "Exiting script."
        exit 0
    fi
    day_number=01
else
    # Find the highest number XX
    highest_number=0
    for dir in "${existing_dirs[@]}"; do
        number=${dir:3}
        if [ "$number" -gt "$highest_number" ]; then
            highest_number=$number
        fi
    done

    # Increment the highest number to get the next challenge dayYY
    day_number=$(printf "%02d" $((highest_number + 1)))

    read -p "Create blank challenge for day$day_number? [y/n]: " response
    if [ "$response" != "y" ]; then
        echo "Exiting script."
        exit 0
    fi
fi

# Create the subdirectory
mkdir "day$day_number"
cd "day$day_number"

# Create blank files
touch input.txt sample_input.txt __init__.py

# Create 'test_sample.py' file
echo "from pathlib import Path

from .solution import part_one, part_two

LINES = Path(__file__).parent.joinpath('sample_input.txt').read_text().splitlines()


def test_part_one():
    assert part_one(LINES) == 0


def test_part_two():
    assert part_two(LINES) == 0" > test_sample.py

# Create 'solution.py' file
echo "from pathlib import Path

LINES = Path(__file__).parent.joinpath('input.txt').read_text().splitlines()

def part_one(lines: list[str]) -> int:
    return 0


def part_two(lines: list[str]) -> int:
    return 0

if __name__ == '__main__':
    print('Part one:', part_one(LINES))
    print('Part two:', part_two(LINES))" > solution.py

echo "Challenge directory 'day$day_number' created with necessary files."

