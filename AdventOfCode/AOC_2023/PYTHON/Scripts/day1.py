import os
import sys
import enum
with open(os.path.join(sys.path[0], "../Inputs/input_day1.txt"), "r") as my_input:
    _INPUT:str = my_input.read()
    _INPUT:list[str] = _INPUT.split("\n")
    #print(_INPUT)

import re

def convert_to_digit(spelled_number:str) -> str:
    number_dict = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }

    return number_dict[spelled_number.lower()] if spelled_number.lower() in number_dict else None


def get_spelled_numbers(row: str) -> list[tuple[str, int]]:
    # Returns a list of strings and their index of spelled numbers contained in a string
    spelled_number_pattern:re.Pattern[str] = re.compile(r'(one|two|three|four|five|six|seven|eight|nine)', re.IGNORECASE)

    return [(convert_to_digit(match.group()), match.start()) for match in spelled_number_pattern.finditer(row)]


def get_digits(row:str) -> list[tuple[str,int]]:
    # Returns a list of strings and their index of digits contained in a string
    digit_pattern:re.Pattern[str] = re.compile(r'\d')
    
    return [(match.group(), match.start()) for match in digit_pattern.finditer(row)]


#---------------------Day Part Definitions -------------------------#

def PROCESS_ROW_PART_1(row:str, sum:int) -> int:
    row_digits:list[tuple[str, int]] = get_digits(row)
    row_combine:str = row_digits[0][0] + row_digits[-1][0] if row_digits  else '0'

    return sum + int(row_combine)


def PROCESS_ROW_PART_2(row:str, sum:int) -> int:
    row_digits:list[tuple[str, int]] = get_digits(row)
    row_digits.extend(get_spelled_numbers(row))
    sorted_digits:list[tuple[str, int]] = sorted(row_digits, key=lambda x: x[1])
    row_combine:str = sorted_digits[0][0] + sorted_digits[-1][0]

    return sum + int(row_combine)


#--------------------- MAIN -------------------------#

absolute_sum_part_1:int = 0
absolute_sum_part_2:int = 0

for row in _INPUT:
    absolute_sum_part_1 = PROCESS_ROW_PART_1(row, absolute_sum_part_1)
    absolute_sum_part_2 = PROCESS_ROW_PART_2(row, absolute_sum_part_2)


# -------------- TESTCASES ------------------ #
potential_input_list:list[str] = ["jvvslnkdk6qnfzjzvseight55eight", "xkbseventwotwogmkxhpmhm42hvvbfchreight", "gcqeightwosix8xdlhrnnbkmsevenqdbrjghz", 
                        "458ninextfjxvgsq5fltdsk6", "rlgsflhxqd5bdbhclmrthree", "twothreemqqbzjn88blvqxbseven", "rqrrdrmlfsixfive6",
                        "eight959tzxkgqjd", "fzrj4","three",  "4nfone5eight", "439", "txdszrn5eight3cqeight1brqr"]
potential_input_list2:list[str] = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", 
                        "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

#for potential_input in potential_input_list2:
#    print("INPUT", potential_input)
##    absolute_sum_part_1 = PROCESS_ROW_PART_1(potential_input, absolute_sum_part_1)
#    absolute_sum_part_2 = PROCESS_ROW_PART_2(potential_input, absolute_sum_part_2)
#    print("--------------------------")


# -------------- RESULTS ------------------ #

print("DAY 1 Part 1: ", absolute_sum_part_1) # ANSWER: 54450
print("DAY 1 Part 2: ", absolute_sum_part_2)