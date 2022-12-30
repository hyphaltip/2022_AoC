#!/usr/bin/env python3
"""Day 8 of advent of code.

Calculate tree cover.
"""
import argparse
import sys


def calculate_vizibility(inputfh, debug=False):
    """Calculate treecover vizibility."""
    matrix = []
    viz = {}

    for line in inputfh:
        line = line.strip()
        if len(line):
            row = []
            for c in line:
                row.append(int(c))
            matrix.append(row)

    #  print(matrix)
    height = len(matrix)
    #  assume this is square matrix
    #  could add a test to better protects
    width = len(matrix[0])
    # a bit brute force, probably could keep track of
    # whether view already obstructed
    visible_trees = 0
    for i in range(height):
        for j in range(width):
            treeheight = matrix[i][j]
            pos = f'{i},{j}'
            viz[pos] = {'height': treeheight,
                        'status': False}

            if i == 0 or i == height-1 or j == 0 or j == width-1:
                # redundant but okay to keep I think
                viz[pos]['status'] = True
            else:
                row = []
                for col in range(0, j):
                    row.append(matrix[i][col])

                #  go left to here
                m = max(row)
                if debug:
                    print(f"max for left side of row {row} is {m}")
                if m < treeheight:
                    viz[pos]['status'] = True
                    continue

                #  go right to edge
                row = []
                for col in range(j+1, width):
                    row.append(matrix[i][col])
                m = max(row)
                if debug:
                    print(f"max for right side of row {row} is {m}")
                if m < treeheight:
                    viz[pos]['status'] = True
                    continue

                #  from top matrix to this tree
                column = []
                for r in range(0, i):
                    column.append(matrix[r][j])
                m = max(column)
                if debug:
                    print(f"max for col {column} is {m}")
                if m < treeheight:
                    viz[pos]['status'] = True
                    continue
                # from below tree to bottom of matrix
                column = []
                for r in range(i+1, height):
                    column.append(matrix[r][j])
                m = max(column)
                if debug:
                    print(f"max for col {column} is {m}")
                if m < treeheight:
                    viz[pos]['status'] = True

    for (pos, tree) in viz.items():
        if debug:
            print(pos, tree)
        if tree['status']:
            visible_trees += 1

    return (visible_trees)


def main():
    """Treetop Tree House."""
    parser = argparse.ArgumentParser(description='Run AoC Day 8')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    parser.add_argument('-v', '--debug', default=False, action=argparse.BooleanOptionalAction,
                        help='debugging statements')
    args = parser.parse_args()

    viztrees = calculate_vizibility(args.input, args.debug)
    print(f'There were {viztrees} trees visible')
    return 0


if __name__ == "__main__":
    main()

# END
