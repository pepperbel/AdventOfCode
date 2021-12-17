import os
import sys
import copy
with open(os.path.join(sys.path[0], "../Inputs/input_day_9.txt"), "r") as my_input:
    _INPUT_1 = my_input.read().split("\n")
    _INPUT_1 = [int(i) for i in _INPUT_1]
    # print(_INPUT_1)


class PREAMBLE(object):
    """ class preamble 
    - property for preamble consisting of 25 numbers
    - calculator for all values definition
    - 
    """

    def __init__(self, input):
        self._preamble = input[:25]  # list of 25 numbers
        self._remaining_inputs = input[25:]
        self.input_range = copy.deepcopy(input[25:])
        self.input_preamble = copy.deepcopy(input[:25])
        self._invalid = 0

        self.part_one()
        self.part_two()

    @property
    def preamble(self):
        return self._preamble

    @preamble.setter
    def preamble(self, numbers):
        self._preamble = numbers

    @property
    def remaining_inputs(self):
        return self._remaining_inputs

    @remaining_inputs.setter
    def remaining_inputs(self, current_range):
        self._remaining_inputs = current_range

    def match_number(self, number):
        for i in self.preamble:
            for j in self.preamble[1:]:
                if not i == j:
                    if i + j == number:
                        return True

        return False

    def update_preamble(self):
        self.preamble = self._preamble[1:]
        self._preamble.append(self.remaining_inputs[0])
        self.remaining_inputs = self._remaining_inputs[1:]

    def part_one(self):
        for i in range(0, len(self.input_range)):
            is_match = self.match_number(self.input_range[i])
            if is_match:
                self.update_preamble()
            else:
                print(
                    "PART ONE {} -- {}".format(self.input_range[i], (i + 26)))
                self._invalid = self.input_range[i]
                break

    def part_two(self):
        pass


day_9 = PREAMBLE(_INPUT_1)
