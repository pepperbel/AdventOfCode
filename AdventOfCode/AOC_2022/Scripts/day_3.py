import string
import os
import sys
from enum import Enum
with open(os.path.join(sys.path[0], "../Inputs/input_day_3.txt"), "r") as my_input:
    _INPUT = my_input.read()
    _INPUT = _INPUT.split("\n")
    #_INPUT2 = [e.append(a) for a in _INPUT]
    # print(_INPUT2)

PRIORITY = string.ascii_letters


def get_priority(c: str):
    return PRIORITY.index(c) + 1


sum_of_priorities = 0
priorities_similar_badges = 0
common_badge = ""
group_counter = 0

for rucksack in _INPUT:

    # Part 1
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]
    shared = [e for e in {*compartment1}.intersection({*compartment2})]
    sum_of_priorities += get_priority(shared[0])

    # Part 2
    group_counter += 1
    if group_counter > 3:
        common_badge = ""
        group_counter = 1

    if group_counter == 2:
        print("GROUP:{} {} {} {}".format(group_counter, _INPUT[_INPUT.index(
            rucksack) - 1], rucksack, _INPUT[_INPUT.index(rucksack) + 1]))
        temp_commons = {e for e in {
            *rucksack}.intersection({*_INPUT[_INPUT.index(rucksack) - 1]})}
        temp_commons2 = {e for e in {
            *rucksack}.intersection({*_INPUT[_INPUT.index(rucksack) + 1]})}
        common_badge = [e for e in {
            *temp_commons}.intersection({*temp_commons2})][0]
        priorities_similar_badges += get_priority(common_badge)


print("PART 1: {}".format(sum_of_priorities))
print("PART 2: {}".format(priorities_similar_badges))
