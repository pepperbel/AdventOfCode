import string
import os
import sys
from enum import Enum
with open(os.path.join(sys.path[0], "../Inputs/input_day_4.txt"), "r") as my_input:
    _INPUT = my_input.read()
    _INPUT = _INPUT.split("\n")
    _INPUT = [list(map(int, e.replace(",", "-").split("-"))) for e in _INPUT]
    # print(_INPUT)

part_1_counter = 0
part_2_counter = 0
for section in _INPUT:
    if section[0] <= section[2] and section[1] >= section[3] or section[0] >= section[2] and section[1] <= section[3]:
        # Condition met if one contains the other entirely
        part_1_counter += 1
        part_2_counter += 1
        continue
    elif section[0] >= section[2] and section[0] <= section[3]:
        part_2_counter += 1
        continue
    elif section[1] >= section[2] and section[1] <= section[3]:
        part_2_counter += 1
        continue
    elif section[2] >= section[0] and section[2] <= section[1]:
        part_2_counter += 1
        continue
    elif section[3] >= section[0] and section[3] <= section[1]:
        part_2_counter += 1
        continue


print("Part 1: ", part_1_counter)
print("Part 2: ", part_2_counter)
