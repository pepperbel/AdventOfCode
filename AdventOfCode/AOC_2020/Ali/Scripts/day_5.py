import os
import sys
import math
with open(os.path.join(sys.path[0], "../Inputs/input_day_5.txt"), "r") as my_input:
    _INPUT_1 = my_input.read()
    _INPUT_1 = _INPUT_1.strip().split("\n")
    #print(_INPUT_1)

_FB_RANGE = [0, 127]
_LR_RANGE = [0, 7]
_BOARDING_PASSES = []

def get_new_range(letter, curr_range):
    middle = curr_range[0] + ((curr_range[1] - curr_range[0]) / 2)
    if letter == "F" or letter == "L":
        curr_range = [curr_range[0], math.floor(middle)]
    elif letter == "B" or letter == "R":
        curr_range = [math.ceil(middle), curr_range[1]]
    else:
        print("Invalid Letter")
    return curr_range


def get_final_value(letter, curr_range):
    if letter == "F" or letter == "L":
        return curr_range[0]
    if letter == "B" or letter == "R":
        return curr_range[1]


_HIGHEST_ID = 0
count = 0

# Returns a list of _BOARDING_PASSES
for entry in _INPUT_1:
    count += 1
    _SEAT_ROW = 0
    _SEAT_COLUMN = 0
    _SEAT_ID = 0

    new_range_fb = _FB_RANGE
    new_range_lr = _LR_RANGE
    entry = [entry[:7], entry[7:]]    

    for row in entry[0]:
        new_range_fb = get_new_range(row, new_range_fb)
    _SEAT_ROW = get_final_value(entry[0][-1], new_range_fb)

    for column in entry[1]:
        new_range_lr = get_new_range(column, new_range_lr)
    _SEAT_COLUMN = get_final_value(entry[1][-1], new_range_lr)
    _SEAT_ID = (_SEAT_ROW * 8) + _SEAT_COLUMN


    _BOARDING_PASSES.append(_SEAT_ID)
    _BOARDING_PASSES.sort()

    if _SEAT_ID > _HIGHEST_ID:
        _HIGHEST_ID = _SEAT_ID


for i, seat in enumerate(_BOARDING_PASSES):
    if (_BOARDING_PASSES[i] + 1) != _BOARDING_PASSES[i + 1]:
        print(_BOARDING_PASSES[i] + 1)
        break

