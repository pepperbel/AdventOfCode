import os
import sys
with open(os.path.join(sys.path[0], "../Inputs/input_day_1.txt"), "r") as my_input:
    _INPUT = my_input.read()
    _INPUT = _INPUT.split("\n\n")
    _CALORIES = []
    for i in _INPUT:
        group = [int(g) for g in i.split('\n')]
        _CALORIES.append(group)
    print(_CALORIES)

most_calories = 0
second_place = 0
third_place = 0

for group in _CALORIES:
    total_calories = 0
    for member in group:
        total_calories += member

    if most_calories < total_calories:
        third_place = second_place
        second_place = most_calories
        most_calories = total_calories
    elif second_place < total_calories:
        third_place = second_place
        second_place = total_calories
    elif third_place < total_calories:
        third_place = total_calories

print("Part 1:: {}".format(most_calories))
print("Second:: {}".format(second_place))
print("Third:: {}".format(third_place))
print("Part 2:: {}".format(most_calories + second_place + third_place))
