#!/usr/bin/env python3
"""Advent of Code Day 1 - Part 2.

Part 2 solved.
"""
import argparse
import sys


def count_calories(inputfh):
    """Count calories from an input filehandle."""
    elves = [0]
    max = 0
    for line in inputfh:
        line = line.strip()
        if len(line) == 0:
            elves.append(0)
            continue
        calorie = int(line.strip())
        elves[-1] += calorie
        if max < elves[-1]:
            max = elves[-1]

    elves = sorted(elves, reverse=True)
    return (elves)


def main():
    """Main calorie counting program."""
    parser = argparse.ArgumentParser(description='Run AoC Day 1')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    args = parser.parse_args()
    elves = count_calories(args.input)
#    for i in (range(len(elves))):
#        print(f'Elf-{i} has {elves[i]} calories')
    topN = elves[0:3]
    print(f'Top 3 eleves are {topN} total calories: {sum(topN)}')
    return 0


if __name__ == "__main__":
    main()
