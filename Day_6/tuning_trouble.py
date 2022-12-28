#!/usr/bin/env python3
"""Day 6 of advent of code.

Tuning trouble. Parts 1 & 2
"""
import argparse
import sys


def find_start_of_packet(line, wordlen=4):
    """Look for words which have all unique characters."""
    for i in range(0, len(line)):
        word = line[i:i+wordlen]
        #  print(i,word)
        unique = len(set(word))
        if unique == wordlen:
            return (i + wordlen)
    return (-1)


def main():
    """Tuning Trouble."""
    parser = argparse.ArgumentParser(description='Run AoC Day 6')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    args = parser.parse_args()
    for line in args.input:
        line = line.strip()
        markerstart = find_start_of_packet(line)
        msgstart = find_start_of_packet(line, 14)
        print(f'marker starts at {markerstart} for "{line}"')
        print(f'message starts at {msgstart}')
    return 0


if __name__ == "__main__":
    main()

# END
