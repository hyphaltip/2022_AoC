#!/usr/bin/env python3
"""Day 8 of advent of code.

Calculate tree cover.
"""
import argparse
import sys


def score_height_list(curheight, col):
    """Score sight lines from trees."""
    val = 0
    for t in col:
        val += 1
        if t >= curheight:
            break
    return (val)


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
    for i in range(height):
        for j in range(width):
            treeheight = matrix[i][j]
            pos = f'{i},{j}'
            viz[pos] = {'height': treeheight,
                        'status': False,
                        'scenic': 0}

            if i == 0 or i == height-1 or j == 0 or j == width-1:
                # redundant but okay to keep I think
                viz[pos]['status'] = True

            else:
                row = []
                #  go left to here
                for col in range(0, j):
                    row.append(matrix[i][col])
                row.reverse()
                left = score_height_list(treeheight, row)

                m = max(row)
                if debug:
                    print(f'left is {left} h={treeheight} for {i},{j} ({row})')
                    print(f"max for left side of row {row} is {m}")
                if m < treeheight:
                    viz[pos]['status'] = True

                #  go right to edge
                row = []
                for col in range(j+1, width):
                    row.append(matrix[i][col])

                right = score_height_list(treeheight, row)

                m = max(row)
                if debug:
                    print(f'right is {right} h={treeheight} for {i},{j} ({row})')
                    print(f"max for right side of row {row} is {m}")
                if m < treeheight:
                    viz[pos]['status'] = True

                #  from top matrix to this tree
                column = []
                for r in range(0, i):
                    column.append(matrix[r][j])
                column.reverse()
                up = score_height_list(treeheight, column)

                m = max(column)
                if debug:
                    print(f'up is {up} h={treeheight} for {i},{j} ({column})')
                    print(f"max for col {column} is {m}")
                if m < treeheight:
                    viz[pos]['status'] = True
                # from below tree to bottom of matrix
                column = []
                for r in range(i+1, height):
                    column.append(matrix[r][j])

                down = score_height_list(treeheight, column)

                m = max(column)
                if debug:
                    print(f'down is {down} h={treeheight} for {i},{j} ({column})')
                    print(f"max for col {column} is {m}")
                if m < treeheight:
                    viz[pos]['status'] = True
                if debug:
                    print(f"{i},{j} u={up} l={left} d={down} r={right}")
                viz[pos]['scenic'] = left * right * up * down

    best_scenic = 0
    visible_trees = 0
    for (pos, tree) in viz.items():
        if debug:
            print(pos, tree)
        if tree['status']:
            visible_trees += 1
        if tree['scenic'] > best_scenic:
            best_scenic = tree['scenic']

    return (visible_trees, best_scenic)


def main():
    """Treetop Tree House."""
    parser = argparse.ArgumentParser(description='Run AoC Day 8')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    parser.add_argument('-v', '--debug', default=False, action=argparse.BooleanOptionalAction,
                        help='debugging statements')
    args = parser.parse_args()

    (viztrees, best) = calculate_vizibility(args.input, args.debug)
    print(f'There were {viztrees} trees visible')
    print(f'The best scenic view score is {best}')

    return 0


if __name__ == "__main__":
    main()

# END
