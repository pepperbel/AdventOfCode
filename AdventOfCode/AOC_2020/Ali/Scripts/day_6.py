import os
import sys
import math
with open(os.path.join(sys.path[0], "../Inputs/input_day_6.txt"), "r") as my_input:
    _INPUT_1 = my_input.read()
    _INPUT_1 = _INPUT_1.split("\n\n")
    #print(_INPUT_1)

_OUPUT_1 = 0
_OUPUT_2 = 0

for group in _INPUT_1:
    group = group.split("\n")
    saved_answer = []
    saved_people = []

    #---------- Part 1 ------------#
    for person in group:
        saved_people.append(person)
        saved_answer += [answer for answer in person if answer not in saved_answer]    
    _OUPUT_1 += len(saved_answer)

    #---------- Part 2 ------------#
    repeated_letters = ""
    for answer in saved_answer:         
        repititions = 0
        required_repetitions = len(saved_people)
        
        for person in saved_people:
            if answer in person:
                repititions += 1
        
        if repititions == required_repetitions:
            repeated_letters += answer
            _OUPUT_2 += 1

print(_OUPUT_1)
print(_OUPUT_2)
