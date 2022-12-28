#!/usr/bin/env python3
"""Day 2 of advent of code.

Score shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
points for shape:
rock: 1
paper: 2
scissors: 3

points to:
win: 6
lose: 0
draw: 3

A=Rock
B=Paper
C=Scissors

X=Rock
Y=Paper
Z=scissors

AX = Rock (them) Rock (self) Draw
AY = Rock (them) Paper (self) Win
AZ = Rock (them) Scissors (self) Lose
"""
import argparse
import sys

self_compare = {"AX": 3, "AY": 6, "AZ": 0,
                "BX": 0, "BY": 3, "BZ": 6,
                "CX": 6, "CY": 0, "CZ": 3}


value_shape = {'X': 1, 'Y': 2, 'Z': 3,
               'A': 1, 'B': 2, 'C': 3,
               'rock': 1, 'paper': 2, 'scissors': 3}

strategy_lookup = {'A': ['Z', 'X', 'Y'],
                   'B': ['X', 'Y', 'Z'],
                   'C': ['Y', 'Z', 'X']}

value_strategy = {'X': 0, 'Y': 3, 'Z': 6}

shape_code = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors',
              'A': 'rock', 'B': 'paper', 'C': 'scissors'}


def compute_RPS(inputfh):
    """Compute the rock paper scissors scoring for part 1."""
    scores = []
    for round in inputfh:
        (opponent, self) = round.upper().split()
        score = self_compare[opponent+self] + value_shape[self]
        #  print(f"o:{opponent} s:{self} score {score}")
        scores.append(score)
    total_score = sum(scores)
    return (scores, total_score)


def compute_RPS_part2(inputfh):
    """Compute the rock paper scissors scoring for part 2."""
    scores = []
    for round in inputfh:
        (opponent, strategy) = round.upper().split()
        strategy_integer = ord(strategy) - ord("X")
        #  print(f'strategy {strategy} integer is {strategy_integer}')
        handplayed = strategy_lookup[opponent][strategy_integer]

        score = value_shape[handplayed] + value_strategy[strategy]
        scores.append(score)
        #  print('opponent is {} ({}) hand shape is {} ({}) score {}'.format(
        #                opponent,  shape_code[opponent],
        #                handplayed, shape_code[handplayed],
        #                score))
        #  print('value strategy is {} ({}) and computed for {}{} is {}'.format(
        #        value_strategy[strategy], strategy,
        #        opponent,handplayed,
        #        self_compare[opponent+handplayed]))

    total_score = sum(scores)
    return (scores, total_score)


def main():
    """Main Rock-Paper-Scissors program."""
    parser = argparse.ArgumentParser(description='Run AoC Day 2')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    args = parser.parse_args()
    (scores, totalscore) = compute_RPS(args.input)
    #  print(f'total score {totalscore} for {scores}')
    print(f'total score {totalscore}')
    args.input.seek(0)

    (scores, totalscore) = compute_RPS_part2(args.input)
    print(f'Part 2, total score {totalscore}')
    return 0


if __name__ == "__main__":
    main()


# END
