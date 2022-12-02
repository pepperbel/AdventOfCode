import os
import sys
from enum import Enum
with open(os.path.join(sys.path[0], "../Inputs/input_day_2.txt"), "r") as my_input:
    _INPUT = my_input.read()
    _INPUT = _INPUT.split("\n")
    # print(_INPUT)


class Scoreboard():

    def __init__(self):
        self._elf_score = 0
        self._person_score = 0

        self.elf_score_dict = self._make_score_dict(True)
        self.person_score_dict = self._make_score_dict(False)

    @property
    def ELF_SCORE(self):
        return self._elf_score

    @ELF_SCORE.setter
    def ELF_SCORE(self, value):
        self._elf_score = value

    @property
    def PERSON_SCORE(self):
        return self._person_score

    @PERSON_SCORE.setter
    def PERSON_SCORE(self, value):
        self._person_score = value

    def evaluate_round(self, elf_value, person_value, part_two=True):

        if part_two:
            person_value = self._calculate_value_pair(elf_value, person_value)

        self._add_choice_point(elf_value)
        self._add_choice_point(person_value)

        self.value_pair = "{}{}".format(elf_value, person_value)
        self.ELF_SCORE += self.elf_score_dict[self.value_pair]
        self.PERSON_SCORE += self.person_score_dict[self.value_pair]

    def _calculate_value_pair(self, elf, person):
        """
        X needs to LOSE
        Y needs to DRAW
        Z needs to WIN
        """
        if person == "X":
            if elf == "A":
                return "Z"
            elif elf == "B":
                return "X"
            elif elf == "C":
                return "Y"
        elif person == "Y":
            if elf == "A":
                return "X"
            elif elf == "B":
                return "Y"
            elif elf == "C":
                return "Z"
        elif person == "Z":
            if elf == "A":
                return "Y"
            elif elf == "B":
                return "Z"
            elif elf == "C":
                return "X"

    def _add_choice_point(self, value):
        if value == "A":
            self.ELF_SCORE += 1
        elif value == "X":
            self.PERSON_SCORE += 1
        elif value == "B":
            self.ELF_SCORE += 2
        elif value == "Y":
            self.PERSON_SCORE += 2
        elif value == "C":
            self.ELF_SCORE += 3
        elif value == "Z":
            self.PERSON_SCORE += 3

    def _make_score_dict(self, elf=True):

        my_dict = {}

        if elf:
            my_dict["AX"] = 3
            my_dict["AY"] = 0
            my_dict["AZ"] = 6
            my_dict["BX"] = 6
            my_dict["BY"] = 3
            my_dict["BZ"] = 0
            my_dict["CX"] = 0
            my_dict["CY"] = 6
            my_dict["CZ"] = 3
        else:
            my_dict["AX"] = 3
            my_dict["AY"] = 6
            my_dict["AZ"] = 0
            my_dict["BX"] = 0
            my_dict["BY"] = 3
            my_dict["BZ"] = 6
            my_dict["CX"] = 6
            my_dict["CY"] = 0
            my_dict["CZ"] = 3

        return my_dict


# ------------ Part 1 --------------- #
SCORE1 = Scoreboard()
for i in _INPUT:
    value_pair = i.split(" ")
    SCORE1.evaluate_round(value_pair[0], value_pair[1], False)
print("Part 1 Answer: {}".format(SCORE1.PERSON_SCORE))

# ------------ Part 2 --------------- #

SCORE2 = Scoreboard()
for i in _INPUT:
    value_pair = i.split(" ")
    SCORE2.evaluate_round(value_pair[0], value_pair[1], True)
print("Part 2 Answer: {}".format(SCORE2.PERSON_SCORE))
