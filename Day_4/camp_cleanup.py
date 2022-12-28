#!/usr/bin/env python3
"""Day 4 of advent of code.

Camp Cleanup
"""
import argparse
import sys


def compute_contained(inputfh):
    """Compute overlap of assignments among elf pairs."""
    completely_contained = 0
    any_overlaps = 0
    for line in inputfh:
        line = line.strip()
        if not line:
            continue
        pair = line.split(",")
        pairSet = []
        for p in pair:
            pairSet.append(set())
            (s, e) = p.split('-')
            for i in range(int(s), int(e)+1):
                pairSet[-1].add(i)

        if (len(pairSet[1] - pairSet[0]) == 0 or
           len(pairSet[0] - pairSet[1]) == 0):
            completely_contained += 1
        if len(pairSet[0] & pairSet[1]) > 0:
            any_overlaps += 1
            #  print(line)
        # print(line,pairSet[0]-pairSet[1],pairSet[1]-pairSet[0])
    return (completely_contained, any_overlaps)


def main():
    """Camp Cleanup."""
    parser = argparse.ArgumentParser(description='Run AoC Day 4')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    args = parser.parse_args()
    (sets_containing, overlaps) = compute_contained(args.input)
    print(f'There are {sets_containing} elf pairs with completely contained assignments')
    print(f'There are {overlaps} elf pairs with any overlaps')
    return 0


if __name__ == "__main__":
    main()

# END
