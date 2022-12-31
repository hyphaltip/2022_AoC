#!/usr/bin/env python3
"""Day 9 of advent of code.

Calculate Rope Swing.
"""
import argparse
import sys


def move_knot(head, pos, debug=False):
    """Move a knot based on the one in front."""
    xdiff = head[0] - pos[0]
    ydiff = head[1] - pos[1]
    xdir = 0 if xdiff == 0 else int(abs(xdiff) / xdiff)
    ydir = 0 if ydiff == 0 else int(abs(ydiff) / ydiff)

    if (abs(xdiff) + abs(ydiff)) > 2:
        pos[0] += xdir
        pos[1] += ydir
        if debug:
            print(f'-> moving knot diagonal xd:{xdiff} yd:{ydiff}')
    else:
        if abs(xdiff) > 1:
            pos[0] += xdir
        if abs(ydiff) > 1:
            pos[1] += ydir
    return (pos)


def calculate_allknots_path(inputfh, knotcount=2, debug=False):
    """Calculate rope tail path through series of moves."""
    knot_positions = []
    knots = []
    for i in range(knotcount):
        knot_positions.append({'0,0': 0})
        knots.append([0, 0])

    for line in inputfh:
        line = line.strip()
        if len(line) == 0:
            continue
        (direction, moves) = line.split()
        moves = int(moves)
        if debug:
            print(f'move {moves} steps in direction {direction}')
            print(f'head: {knots[0]}, tail: {knots[1]}')
        while moves > 0:
            if direction == 'R':
                knots[0][0] += 1
            elif direction == 'L':
                knots[0][0] -= 1
            elif direction == 'U':
                knots[0][1] += 1
            elif direction == 'D':
                knots[0][1] -= 1
            else:
                print(f"unknown direction '{direction}'")
                continue

            for i in range(1, knotcount):
                knots[i] = move_knot(knots[i-1], knots[i], debug)
                knot_positions[i][f"{knots[i][0]},{knots[i][1]}"] = 1
            moves -= 1
    if debug:
        print(knot_positions)
    return (knot_positions)


def calculate_tail_path(inputfh, debug=False):
    """Calculate rope tail path through series of moves."""
    knot_positions = {'0,0': 1}
    head = [0, 0]
    tail = [0, 0]

    for line in inputfh:
        line = line.strip()
        if len(line) == 0:
            continue
        (direction, moves) = line.split()
        moves = int(moves)
        if debug:
            print(f'move {moves} steps in direction {direction}')
            print(f'head: {head}, tail: {tail}')
        while moves > 0:
            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            else:
                print(f"unknown direction '{direction}'")
                continue
            tail = move_knot(head, tail, debug)
            if debug:
                print(f'm; head: {head}, tail: {tail}')
            knot_positions[f"{tail[0]},{tail[1]}"] = 1
            moves -= 1
    if debug:
        print(knot_positions)
    return (knot_positions)


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
    args.input.seek(0)
    knot_count = 10
    (lastknot) = calculate_allknots_path(args.input, knot_count, args.debug)
    if args.debug:
        print(lastknot)
    print(f'After allknots knot: {knot_count-1} had {len(lastknot[knot_count-1])} unique tail positions')
    return 0


if __name__ == "__main__":
    main()

# END
