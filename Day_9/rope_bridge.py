#!/usr/bin/env python3
"""Day 9 of advent of code.

Calculate Rope Swing.
"""
import argparse
import sys


def calculate_tail_path(inputfh, debug=False):
    """Calculate rope tail path through series of moves."""
    tail_positions = {'0,0': 1}
    (head_x, head_y) = (0, 0)
    (tail_x, tail_y) = (0, 0)

    for line in inputfh:
        line = line.strip()
        if len(line) == 0:
            continue
        (direction, moves) = line.split()
        moves = int(moves)
        if debug:
            print(f'move {moves} steps in direction {direction}')
        while moves > 0:
            if direction == 'R':
                head_x += 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'U':
                head_y += 1
            elif direction == 'D':
                head_y -= 1
            else:
                print(f"unknown direction '{direction}'")
                continue

            xdiff = head_x - tail_x
            xdir = 0 if xdiff == 0 else int(abs(xdiff) / xdiff)
            ydiff = head_y - tail_y
            ydir = 0 if ydiff == 0 else int(abs(ydiff) / ydiff)
            if debug:
                print(f"xdiff {xdiff}, ydiff {ydiff}")
            if (abs(xdiff) + abs(ydiff)) > 2:
                tail_x += xdir
                tail_y += ydir
            else:
                if abs(xdiff) > 1:
                    tail_x += xdir
                if abs(ydiff) > 1:
                    tail_y += ydir
            if debug:
                print(f'head: {head_x},{head_y} tail: {tail_x},{tail_y}')
            tail_positions[f"{tail_x},{tail_y}"] = 1
            moves -= 1
    if debug:
        print(tail_positions)
    return (tail_positions)


def main():
    """Rope moves calculator."""
    parser = argparse.ArgumentParser(description='Run AoC Day 8')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    parser.add_argument('-v', '--debug', default=False, action=argparse.BooleanOptionalAction,
                        help='debugging statements')
    args = parser.parse_args()

    (positions) = calculate_tail_path(args.input, args.debug)
    print(f'There were {len(positions)} tail positions')
    return 0


if __name__ == "__main__":
    main()

# END
