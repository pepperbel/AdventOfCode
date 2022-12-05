import os
import sys
import copy


def sort_array(input_array):
    input_array.reverse()
    ruler = input_array[0]
    crates = input_array[1:]

    new_array = []

    for i in range(0, len(ruler)):
        temp_list = []
        for row in crates:
            if ruler[i] != "-" and row[i] != "-":
                temp_list.append(row[i])

        if len(temp_list) > 1:
            new_array.append(temp_list)

    return new_array


with open(os.path.join(sys.path[0], "../Inputs/input_day_5.txt"), "r") as my_input:
    _INPUT = my_input.read()
    _RULES = _INPUT.replace("move ", "").replace(
        " from ", "").replace(" to ", "").split("\n")[10:]
    _RULES = [e for e in _RULES]
    _STACKS = [e.replace(" ", "-") for e in _INPUT.split("\n")[:9]]
    _STACKS = sort_array(_STACKS)


class CargoCrane():

    def __init__(self, crates):
        self._crates = crates

    @property
    def CRATES(self):
        return self._crates

    @CRATES.setter
    def CRATES(self, value):
        self._crates = value

    def move_crates(self, quantity, take_from, move_to, part_one=True):
        moved_crates = self.CRATES[take_from -
                                   1][len(self.CRATES[take_from - 1]) - quantity:]
        if part_one:
            moved_crates.reverse()

        for n in range(0, quantity):
            self.CRATES[move_to - 1].append(moved_crates[n])

        self.CRATES[take_from - 1] = self.CRATES[take_from - 1][:-quantity]

    def get_top_of_stacks(self):
        top_stacks = ""
        for stack in self.CRATES:
            top_stacks += stack[-1]

        return top_stacks


mover_boi_9000 = CargoCrane(copy.deepcopy(_STACKS))
mover_boi_9001 = CargoCrane(copy.deepcopy(_STACKS))

print(_STACKS)

for rule in _RULES:
    num_crates = int(rule[:-2])
    rule = [int(n) for n in rule]
    source = rule[-2]
    target = rule[-1]
    mover_boi_9000.move_crates(num_crates, rule[-2], rule[-1], True)
    mover_boi_9001.move_crates(num_crates, rule[-2], rule[-1], False)

print("Part 1: ", mover_boi_9000.get_top_of_stacks())
print(_STACKS)


#mover_boi_9001 = CargoCrane(_STACKS)
#mover_boi_9000.move_crates(num_crates, rule[-2], rule[-1], False)
print("Part 2: ", mover_boi_9001.get_top_of_stacks())
