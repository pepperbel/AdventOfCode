# https://adventofcode.com/2023/day/3
# region ---- imports and inputs ----

import re
import AOC_Utilities as utils

INPUT = utils.DataManager(__file__).get_data(splitlines=True)
TESTCASES:list[str] = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
            ]

# endregion -------------------------

class RowAttributes(object):

    def __init__(self, row:str) -> None:
        self.game_id_str:str = self._get_card_id(row.split(":")[0])
        self.game_id_index:int = int(self.game_id_str) - 1
        self.lottery_numbers:list[int] = self._get_numbers_from_string(row.split(":")[1].split("|")[0])
        self.input_numbers:list[int] = self._get_numbers_from_string(row.split(":")[1].split("|")[1])

        self.winning_numbers:list[int] = self._get_winning_numbers()
        self.card_value:int = self._get_card_value()

        self.possible_copies:list[int] = self._get_card_copy_ids()

    def _get_card_id(self, full_str:str) -> str:
        return full_str.split(" ")[1].strip()

    def _get_numbers_from_string(self, digits:str) -> list[int]:
        number_array = digits.split(" ")
        return [int(item) for item in number_array if item != '']
    
    def _get_winning_numbers(self) -> list[int]:
        set1 = set(self.lottery_numbers)
        set2 = set(self.input_numbers)
        common_elements = list(set1.intersection(set2))
        return common_elements
    
    def _get_card_value(self) -> int:
        if len(self.winning_numbers) >= 1:
            value:int = 1
            for digit in range(1, len(self.winning_numbers)):
                value += value
            return value
        else:
            return 0

    def _get_card_copy_ids(self) -> list[int]:
        # Returns an index for a list, in oprder to get string value for card, need to +1 to all
        # Card 1 will have an index of 0
        num_copies = len(self.winning_numbers)
        id_list:list[int] = []
        for i in range(0, num_copies):
            id_list.append(self.game_id_index + i + 1)

        return id_list

    def DEBUG_print_attributes(self):
        print("-------- IDs and Copies --------")
        print("GAME ID STR: ", self.game_id_str)
        print("GAME ID INDEX: ", self.game_id_index)
        print("COPY INDEX IDs: ", self.possible_copies)
        print("-------- Numbers on Card --------")
        print("LOTTERY NUMS: ", self.lottery_numbers)
        print("INPUT NUMS: ", self.input_numbers)
        print("-------- Winning Part 1 --------")
        print("WINNING NUMS: ", self.winning_numbers)
        print("CARD VALUE: ", self.card_value)

def get_row_attributes(id:int):
    return RowAttributes(INPUT[id])


card_value_part_1 = 0
list_of_copies = []
scratchcard_count_part_2 = 0
win = True

for row in TESTCASES:
    row_attr:RowAttributes = RowAttributes(row)
    card_value_part_1 += row_attr.card_value
    row_attr.DEBUG_print_attributes()

    # PART 2
    num_copies = len(row_attr.winning_numbers)
    while win:
        if num_copies > 0:
            num_copies -= 1

            list_of_copies += 

        else:
            win = False

print("DAY 4 Part 1: ", card_value_part_1) # ANSWER == 18619
print("DAY 4 Part 2: ", card_value_part_1) # ANSWER == 


# 1. get a list of all possible copies and originals


