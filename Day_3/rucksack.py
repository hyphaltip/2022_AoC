#!/usr/bin/env python3
"""Day 3 of advent of code.

Rucksack reorganization
"""
import argparse
import sys


def compute_priority(item):
    """Determine priority score for the item code based on instructions."""
    if not item[0].isalpha():
        return 0
    elif item[0].islower():
        return ord(item[0]) - ord('a') + 1
    else:
        return ord(item[0]) - ord('A') + 27


def compute(inputfh):
    """Compute the rock paper scissors scoring for part 1."""
    sacks = []
    for contents in inputfh:
        contents = contents.strip()
        count = len(contents)
        if count % 2 != 0:
            print(f"sack {contents}, has non-even count of items")
            break
        half = int(count / 2)

        left = set(contents[0:half])
        right = set(contents[half:])
        score = 0
        for item in (left & right):
            score = compute_priority(item)
            print(item, score)
        sacks.append(score)
    return (sacks, sum(sacks))


def compute_triples(inputfh):
    """Compute the rock paper scissors triplet of elfpacks scoring for part 2."""
    sacks = []
    for contents in inputfh:
        sacks.append(contents.strip())
    scores = []
    for i in range(0, len(sacks), 3):
        for badge in set(sacks[i+0]) & set(sacks[i+1]) & set(sacks[i+2]):
            s = compute_priority(badge)
            #  print(f'score: {s} for badge {badge}')
            scores.append(s)
    return (sum(scores))


def main():
    """Main Rucksack Reorganization."""
    parser = argparse.ArgumentParser(description='Run AoC Day 3')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    args = parser.parse_args()

    (sacks, total_score) = compute(args.input)
    print(f'sacks:\n{sacks}\nscore is {total_score}')
    args.input.seek(0)
    (badge_score) = compute_triples(args.input)
    print(f'badge score is {badge_score}')
    return 0


if __name__ == "__main__":
    main()

# END
