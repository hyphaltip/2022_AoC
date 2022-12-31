#!/usr/bin/env python3
"""Day 5 of advent of code.

Supply Stacks - Part 2.
Cargo crane 9001
"""
import argparse
import collections
import re
import sys


def move_crates(inputfh):
    """Move crates according to the input."""
    # parse header
    #  initialize with an empty stack at 0 since we won't use that
    stacks = [[]]
    inheader = True
    for line in inputfh:
        if inheader:
            if re.match(r'^\s+$', line):
                inheader = False
                # will reverse the stacks so that the top of stack is to the right so we can use
                # pop/push commands
                #  print(stacks[1:])
                for i in range(1, len(stacks)):
                    stacks[i] = collections.deque(stacks[i])
                #  print(stacks[1:])
                continue
            stack = 1
            #  data are in sets of 4 columns assuming single letter codes
            for i in range(0, len(line), 4):
                if len(stacks) <= stack:
                    stacks.append([])
                crate = line[i+0:i+4]
                m = re.match(r'\[([^\]]+)\]', crate)
                if m:
                    #  print(stack,m.group(1))
                    stacks[stack].append(m.group(1))
                stack += 1
        else:
            if len(line) == 0:
                # skip empty lines
                continue
            m = re.match(r'move (\d+) from (\d+) to (\d+)', line)
            print(f'Before: {stacks[1:]}')
            if m:
                count = int(m.group(1))
                src = int(m.group(2))
                dest = int(m.group(3))
                #  print(f'move {count} crates from src: {src} to {dest}')
                #  add the source crates preserving their order
                for i in range(count, 0, -1):
                    stacks[dest].extendleft(stacks[src][i-1])
                for i in range(0, count):
                    stacks[src].popleft()

                print(f'After: {stacks[1:]}')
            else:
                print(f"cannot match '{line}'")

    last_crates = []
    for i in range(1, len(stacks)):
        # get left most crate
        last_crates.append(stacks[i].popleft())
    return (last_crates)


def main():
    """Camp Cleanup."""
    parser = argparse.ArgumentParser(description='Run AoC Day 5')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    args = parser.parse_args()
    (last_crates) = move_crates(args.input)
    print('The last crates in the stacks are "{}"'.format("".join(last_crates)))

    return 0


if __name__ == "__main__":
    main()

# END
