import os
import sys
with open(os.path.join(sys.path[0], "../Inputs/input_day2.txt"), "r") as my_input:
    _INPUT:str = my_input.read()
    _INPUT:list[str] = _INPUT.split("\n")
    #print(_INPUT)

import re

class row_attributes(object):

    def __init__(self, row:str, success_key:dict) -> None:
        self.game_id:int = int(row.split(":")[0].replace("Game", "").strip())
        self.sets = row.split(":")[1]
        self.num_sets:int = len(self.sets)
        self.success_key = success_key

    def get_matches(self, color:str):
        return re.findall(r'\b(\d+)\s+{}\b'.format(re.escape(color)), self.sets)

    def get_highest_color_value(self, color:str):
        return max([int(c) for c in self.get_matches(color)])

    def get_color_success(self, color:str):
        success = all(int(value) <= self.success_key[color] for value in self.get_matches(color))
        return success

    def get_multiplied_colors(self):
        value = self.get_highest_color_value("red")
        value *= self.get_highest_color_value("blue")
        value *= self.get_highest_color_value("green")

        return value

    def is_row_successful(self) -> bool:
        success = all([self.get_color_success("red"), self.get_color_success("green"), self.get_color_success("blue")])
        return success


tests:list[str] = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


success_key = {
    "red" : 12,
    "green": 13,
    "blue": 14
}
sum_of_successes = 0
sum_of_multipliers = 0
success_list = []

for row in _INPUT:
    row_attr:row_attributes = row_attributes(row, success_key)

    if row_attr.is_row_successful():
        success_list.append(row_attr.game_id)
        sum_of_successes += row_attr.game_id
    
    sum_of_multipliers += row_attr.get_multiplied_colors()
        



print("TOTAL PART 1: ", sum_of_successes) # Part 1 ANSWER: 3099
print("TOTAL PART 2: ", sum_of_multipliers) # Part 2 ANSWER: 72970






