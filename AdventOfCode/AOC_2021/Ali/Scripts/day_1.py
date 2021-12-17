import os
import sys
import math
with open(os.path.join(sys.path[0], "../Inputs/input_day_1.txt"), "r") as my_input:
    _INPUT = my_input.read()
    _INPUT = _INPUT.split("\n")
    _INPUT = [int(i) for i in _INPUT]
    # print(_INPUT)


def part_one():
    _OUTPUT_1 = 0
    for i in range(0, len(_INPUT)):
        if i > 0:
            if _INPUT[i] - _INPUT[i - 1] > 0:
                # print("increase: {} {} {}".format(
                #    _INPUT[i], _INPUT[i-1], (_INPUT[i] - _INPUT[i-1])))
                _OUTPUT_1 += 1

    print("Part 1: {}".format(_OUTPUT_1))


def part_two():
    _OUTPUT_2 = 0
    for i in range(0, len(_INPUT)):
        if i > 0 and (i+3) < len(_INPUT):

            chunk_1 = _INPUT[i] + _INPUT[i + 1] + _INPUT[i + 2]
            chunk_2 = _INPUT[i + 1] + _INPUT[i + 2] + _INPUT[i + 3]
            diff = chunk_2 - chunk_1

            if diff > 0:
                # print(diff)
                _OUTPUT_2 += 1

    print("Part 2: {}".format(_OUTPUT_2))


part_one()
part_two()
