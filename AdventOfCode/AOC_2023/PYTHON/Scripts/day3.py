import os
import sys
with open(os.path.join(sys.path[0], "../Inputs/input_day3.txt"), "r") as my_input:
    _INPUT:str = my_input.read()
    _INPUT:list[str] = _INPUT.split("\n")
    #print(_INPUT)

import re
SYMBOL_KEY = re.compile(r'[^\w\d.]')

TESTCASES:list[str] = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."
            ]

TESTCASES_CUSTOM:list[str] = [
            "467.114...",
            "...*..*...",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."
            ]

class RowAttributes(object):

    def __init__(self, row_set) -> None:

        self.grid:dict[str,list] = {
            "N": [],
            "M": [],
            "S": [],
        }

        self.multiplied_gears:int = 0

        self._top_row:str = row_set[0]
        self._middle_row:str = row_set[1]
        self._bottom_row:str = row_set[2]

        self.symbol_indices:list[str, int] = self._get_symbols_index_in_row() if len(self._get_symbols_index_in_row()) >= 1 else None

    # INTERNAL FUNCS

    def _get_symbols_index_in_row(self) -> tuple[str, int]:
        # Returns all symbols and their indexes in the row 

        # Get Indexes of symbol positions
        matches:re.Iterator[re.Match[str]] = SYMBOL_KEY.finditer(self._middle_row)

        #Get Symbols and Indices
        symbols_with_indices:tuple[str, int] = [(match.group(), match.start()) for match in matches]

        return symbols_with_indices

    def _get_index_range_and_number(self, row:str, start_index:int) ->list[list[int], str]:
        left_index:int = int(start_index)
        right_index:int = int(start_index)

        #  Move index to left until a non-digit is found
        while left_index >= 0 and row[left_index].isdigit():
            left_index -= 1

        # Move index to right until a non-digit is found
        while right_index < len(row) and row[right_index].isdigit():
            right_index += 1

        # Exclude non-digit characters
        left_index += 1
        right_index -= 1

        return [[left_index, right_index], row[left_index:right_index + 1]]

    def _get_dir_info(self, row:str, index:int) -> list[list[int], str]:
        # Returns a list that has the coordinates of a number in index ranges, and the number
        if row[index].isdigit(): 
                return (self._get_index_range_and_number(row, index))

    def _append_unique(self, dir:str, value:list[list[int], str]) -> None:
        # Makes sure only numbers and their coordinates are mapped that haven't already been mapped
        if value not in self.grid[dir]:
            self.grid[dir].append(value)

    def _get_multipled_gears(self, symbol_index:int) -> list[int, list[int]]:
        #Checks for gears, and if found returns the multiplied values
        multiply_list:list[str] = []

        # hate this...needs to be cuter, but honestly I'm tired
        for dir, items in self.grid.items():
                for item in items:
                    if item != None:
                        if item[0][0] >= symbol_index - 1 or item[0][1] >= symbol_index - 1:
                            if item[0][0] <= symbol_index + 1 or item[0][1] <= symbol_index + 1:
                                multiply_list.append(item[1])

        if len(multiply_list) > 2:
            print("EMERGENCY, YOU HAVE NOT HANDLED THIS EDGE CASE....GOOD GOD HELP YOU")
            return 0
        elif len(multiply_list) < 2:
            return 0 
        else:
            return int(multiply_list[0]) * int(multiply_list[1])

    # EXTERNAL FUNCS

    def map_adjacent(self) -> None:
        # Populates the North, Middle and South matches into a dictionary
        # Checks for Gears
        for symbol in self.symbol_indices:

            # NORTH
            self._append_unique("N", self._get_dir_info(self._top_row, symbol[1] - 1))
            self._append_unique("N", self._get_dir_info(self._top_row, symbol[1]))
            self._append_unique("N", self._get_dir_info(self._top_row, symbol[1] + 1))

            # MIDDLE
            self._append_unique("M", self._get_dir_info(self._middle_row, symbol[1] - 1))
            self._append_unique("M", self._get_dir_info(self._middle_row, symbol[1] + 1))

            # SOUTH
            self._append_unique("S", self._get_dir_info(self._bottom_row, symbol[1] - 1))
            self._append_unique("S", self._get_dir_info(self._bottom_row, symbol[1]))
            self._append_unique("S", self._get_dir_info(self._bottom_row, symbol[1] + 1))

            if symbol[0] == "*":
                self.multiplied_gears += self._get_multipled_gears(symbol[1])

    def add_values_of_rows(self) -> list[int, list[int]]:
        total_sum:int = 0
        debug_nums:list[int] = []

        for direction, dir_info in self.grid.items():
            for value in dir_info:
                if value != None:
                    number:int = value[1]
                    debug_nums.append(int(number))
                    total_sum += int(number)

        return [total_sum, debug_nums]

    # DEBUG FUNCS
    def DEBUG_print_grid_around_symbol(self):
        print("SYMBOLS: ", self.symbol_indices)
        print(self.grid)
    
    def DEBUG_print_row_set(self):
        print("TOP    ROW: ", self._top_row)
        print("FOCUS  ROW: ", self._middle_row)
        print("BOTTOM ROW: ", self._bottom_row)

    def DEBUG_print_sum_of_row_set(self):
        sum, nums = self.add_values_of_rows()
        print("NUMS of ROW SET: ", nums)
        print("SUM OF 1 ROW_SET: ", sum)


def compare_for_duplicates(current_list, previous_list):
    # Strips current_list of all duplicates found matching on the previous list
    for item in previous_list:
        if item in current_list:
            current_list.remove(item)

    return current_list

def execute_day_3(ROWS:list[str]) -> tuple[int]:

    total_sum_part_1:int = 0
    total_sum_part_2:int = 0
    previous_bottom_row:list = []

    for i in range(1, len(ROWS)):

        if i == 0 and len(ROWS) - 1 != i:
            # FIRST ROW
            row_set = ["....", ROWS[i], ROWS[i+1]]
        if i >= 1 and len(ROWS) - 1 != i:
            row_set = [ROWS[i-1], ROWS[i], ROWS[i+1]]
        elif i == len(ROWS) - 1:
            # LAST ROW
            row_set = [ROWS[i-1], ROWS[i], "...."]


        #print("----------Start {}-----------".format(i))

        row_attr:RowAttributes = RowAttributes(row_set)
        if row_attr.symbol_indices == None:
            continue

        row_attr.map_adjacent()

        if len(previous_bottom_row) != 0:
            row_attr.grid["S"] = compare_for_duplicates(row_attr.grid["S"], previous_bottom_row[1])
        
        previous_bottom_row = [i, row_attr.grid["S"]]

        # PART 1 & 2
        total_sum_part_1 += row_attr.add_values_of_rows()[0]
        total_sum_part_2 += row_attr.multiplied_gears

        # DEBUG
        #row_attr.DEBUG_print_grid_around_symbol()
        #row_attr.DEBUG_print_row_set()
        #row_attr.DEBUG_print_sum_of_row_set()

    return total_sum_part_1, total_sum_part_2


sum_part_1, sum_part_2 = execute_day_3(_INPUT)

print("DAY 3 PART 1: ", sum_part_1) # ANSWER PART 1 == 525911
print("DAY 3 PART 2: ", sum_part_2) # ANSWER PART 2 == 75805607