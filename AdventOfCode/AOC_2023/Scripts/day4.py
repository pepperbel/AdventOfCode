# https://adventofcode.com/2023/day/4
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

class Scratchcard(object):

    def __init__(self, row:str) -> None:
        self.game_id:str = self._get_card_id(row.split(":")[0])
        self.win_key_numbers:list[int] = self._get_numbers_from_string(row.split(":")[1].split("|")[0])
        self.input_numbers:list[int] = self._get_numbers_from_string(row.split(":")[1].split("|")[1])

        self.winning_numbers:list[int] = self._get_winning_numbers()
        self.card_value:int = self._get_card_value()

        self.copies_created:int = 1

    def _get_card_id(self, full_str:str) -> str:
        return full_str.split(" ")[1].strip()

    def _get_numbers_from_string(self, digits:str) -> list[int]:
        number_array = digits.split(" ")
        return [int(number) for number in number_array if number != '']
    
    def _get_winning_numbers(self) -> list[int]:
        set1 = set(self.win_key_numbers)
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

    def DEBUG_print_attributes(self):
        print("-------- IDs and Copies --------")
        print("GAME ID STR: ", self.game_id)
        print("-------- Numbers on Card --------")
        print("WIN KEY NUMS: ", self.win_key_numbers)
        print("INPUT NUMS: ", self.input_numbers)
        print("-------- Winning Part 1 --------")
        print("WINNING NUMS: ", self.winning_numbers)
        print("CARD VALUE: ", self.card_value)

# ----------------- MAIN --------------------- #

def get_scratchcards(input:list[str]) -> list[Scratchcard]:
    return [Scratchcard(row) for row in input]


def execute_day_4_part_1(cards) -> int:

    counter_part_1 = 0

    for current_card in cards:
        counter_part_1 += current_card.card_value
    
    return counter_part_1


def execute_day_4_part_2(cards) -> int:

    counter_part_2 = 0
    

    for current_card in cards:
        for i in range(len(current_card.winning_numbers)):
            index = scratchcards.index(current_card) + 1 + i
            scratchcards[index].copies_created += current_card.copies_created

    for current_card in scratchcards:
        counter_part_2 += current_card.copies_created
    
    return counter_part_2


scratchcards:list[Scratchcard] = get_scratchcards(INPUT)
print("DAY 4 Part 1: ", execute_day_4_part_1(scratchcards)) # ANSWER == 18619
print("DAY 4 Part 2: ", execute_day_4_part_2(scratchcards)) # ANSWER == 8063216



