#!/usr/bin/env python3
"""Day 9 of advent of code.

Calculate Rope Swing.
"""
import argparse
import sys


def calculate_rope_path(inputfh, debug=False):
    """Calculate rope tail path through series of moves."""
    grid = []
    positions = 0
    for line in inputfh:
        line = line.strip()
        if len(line) == 0:
            continue
        (direction, moves) = line.split()

    return (grid, positions)


def main():
    """Rope moves calculator."""
    parser = argparse.ArgumentParser(description='Run AoC Day 8')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    parser.add_argument('-v', '--debug', default=False, action=argparse.BooleanOptionalAction,
                        help='debugging statements')
    args = parser.parse_args()

    (grid, count) = calculate_rope_path(args.input, args.debug)

    return 0


if __name__ == "__main__":
    main()

# END
