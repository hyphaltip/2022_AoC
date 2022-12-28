#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Day 3 of advent of code:

Rucksack reorganization

"""
import argparse
import sys


def compute_priority(item):
    if not item[0].isalpha():
        return 0
    elif item[0].islower():
        return ord(item[0]) - ord('a') + 1
    else:
        return ord(item[0]) - ord('A') + 27

def compute (inputfh):
    """compute the rock paper scissors scoring for part 1"""
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
    return (sacks,sum(sacks))

def compute_triples (inputfh):
    sacks = []
    for contents in inputfh:
        
def main():
    """ Main Rucksack Reorganization """
    parser = argparse.ArgumentParser(
    description='Run AoC Day 3')
    parser.add_argument('-i','--input', type=argparse.FileType('r'), default=sys.stdin,
                    help='Input file (or by stdin)')
    args = parser.parse_args()

    (sacks,total_score) = compute(args.input)
    print(f'sacks:\n{sacks}\nscore is {total_score}')
    #args.input.seek(0)

    return 0

if __name__ == "__main__":
    main()
