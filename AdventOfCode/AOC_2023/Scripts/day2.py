# https://adventofcode.com/2023/day/2
# region ---- imports and inputs ----

import re
import AOC_Utilities as utils

DATA = utils.DataManager(__file__, debug=True)
INPUT = DATA.get_data(splitlines=True,)

import re

# endregion -------------------------

class RowAttributes(object):

    def __init__(self, row:str, success_key:dict) -> None:
        self.game_id:int = int(row.split(":")[0].replace("Game", "").strip())
        self.sets:list[str] = row.split(":")[1]
        self.num_sets:int = len(self.sets)
        self.success_key:dict = success_key

    def _get_matches(self, color:str) -> list[str]:
        return re.findall(r'\b(\d+)\s+{}\b'.format(re.escape(color)), self.sets)

    def _get_highest_color_value(self, color:str) -> int:
        return max([int(c) for c in self._get_matches(color)])

    def _get_color_success(self, color:str) -> bool:
        success:bool = all(int(value) <= self.success_key[color] for value in self._get_matches(color))
        return success

    def get_multiplied_colors(self) -> int:
        value:int = self._get_highest_color_value("red")
        value *= self._get_highest_color_value("blue")
        value *= self._get_highest_color_value("green")

        return value

    def is_row_successful(self) -> bool:
        success:bool = all([self._get_color_success("red"), self._get_color_success("green"), self._get_color_success("blue")])
        return success


tests:list[str] = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


success_key:dict = {
    "red" : 12,
    "green": 13,
    "blue": 14
}
sum_of_successes:int = 0
sum_of_multipliers:int = 0

for row in INPUT:

    row_attr:RowAttributes = RowAttributes(row, success_key)

    if row_attr.is_row_successful():

        sum_of_successes += row_attr.game_id
    
    sum_of_multipliers += row_attr.get_multiplied_colors()
        

print("TOTAL PART 1: ", sum_of_successes) # Part 1 ANSWER: 3099
print("TOTAL PART 2: ", sum_of_multipliers) # Part 2 ANSWER: 72970






