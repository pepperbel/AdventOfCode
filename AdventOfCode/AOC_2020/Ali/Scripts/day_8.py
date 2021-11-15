import os
import sys
import copy

with open(os.path.join(sys.path[0], "../Inputs/input_day_8.txt"), "r") as my_input:
    _INPUT_1 = my_input.read().split("\n")
    _INPUT_1 = [i.split(" ") for i in _INPUT_1]
    # print(_INPUT_1)


class data_entry(object):
    def __init__(self, data, index):
        self.command = data[0]  # acc, jmp, nop
        self.operation = data[1]  # +/-int
        self.index = index
        self.used = False  # has come up before

    @property
    def info(self):
        return "{} {} {} {}".format(self.command, self.operation, self.index, self.used)


_DATA = []
for i in range(0, len(_INPUT_1)):
    _DATA.append(data_entry(_INPUT_1[i], i))

finished = False


def run_accumulator(data):

    data_copy = copy.deepcopy(data)
    _ACCUMULATOR = 0
    is_used = False
    index = 0
    while not is_used:
        try:
            if data_copy[index].used == False:
                data_copy[index].used = True
                if data_copy[index].command == "acc":
                    _ACCUMULATOR += int(data_copy[index].operation)
                    index += 1
                elif data_copy[index].command == "jmp":
                    index += int(data_copy[index].operation)
                elif data_copy[index].command == "nop":
                    index += 1
            else:
                is_used = True
                return _ACCUMULATOR
        except:
            part_two = _ACCUMULATOR
            print(part_two)
            is_used = True
            return _ACCUMULATOR


part_one = run_accumulator(_DATA)
print(part_one)
_DATA_copy = copy.deepcopy(_DATA)
for i in range(0, len(_DATA)):
    if _DATA_copy[i].command == "jmp":
        _DATA_copy[i].command = "nop"
        part_two = run_accumulator(_DATA_copy)

    elif _DATA_copy[i].command == "nop":
        _DATA_copy[i].command = "jmp"
        part_two = run_accumulator(_DATA_copy)
    else:
        if _DATA_copy[i].command != "acc":
            print(i, _DATA_copy[i].info)

    if finished:
        break

    _DATA_copy = copy.deepcopy(_DATA)

print(part_two)
