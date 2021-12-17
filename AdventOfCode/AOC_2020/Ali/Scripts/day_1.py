import os
import sys

_INPUT =  open(os.path.join(sys.path[0], "../Inputs/input_day_1.txt"), "r")
_output = 0
_number = []


for line in _INPUT:
    number = int(line)
    _number.append(number)

for num in range(0, len(_number)):
    remaining_number = _number[num:]

    for comparer in range(0, len(remaining_number)):
        remaining_number_2 = remaining_number[comparer:]

        for comparer_2 in remaining_number_2:

            if int(_number[num]) + int(remaining_number[comparer]) + int(comparer_2)== 2020: 
                print(_number[num], remaining_number[comparer], comparer_2, "woop")
                _OUTPUT = _number[num] * remaining_number[comparer] * comparer_2

print(_OUTPUT)
    