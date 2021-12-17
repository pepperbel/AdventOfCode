import os
import sys
import math
with open(os.path.join(sys.path[0], "../Inputs/input_day_2.txt"), "r") as my_input:
    _INPUT = my_input.read()
    _INPUT = _INPUT.split("\n")
    _INPUT = [i.split(" ") for i in _INPUT]
    _INPUT = [[i[0], int(i[1])] for i in _INPUT]
    # print(_INPUT)


def part_one():
    depth = 0
    distance = 0

    for command in _INPUT:
        if command[0] == 'forward':
            distance += command[1]
        elif command[0] == 'up':
            depth -= command[1]
        elif command[0] == 'down':
            depth += command[1]

    print("Part One: {} * {} = {}".format(distance, depth, (distance * depth)))


def part_two():
    depth = 0
    distance = 0
    aim = 0

    for command in _INPUT:
        if command[0] == 'forward':
            distance += command[1]
            depth += aim * command[1]
        elif command[0] == 'up':
            aim -= command[1]
        elif command[0] == 'down':
            aim += command[1]

    print("Part Two: {} * {} = {}".format(distance, depth, (distance * depth)))


part_one()
part_two()
