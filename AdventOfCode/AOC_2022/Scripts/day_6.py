import os
import sys

with open(os.path.join(sys.path[0], "../Inputs/input_day_6.txt"), "r") as my_input:
    _INPUT = my_input.read()


def marker_check(contestor):
    char_count = 2

    for char in contestor:
        char_count = contestor.count(char)
        if char_count > 1:
            #print(char_count, char, " FALSE")
            return False

    if char_count == 1:
        #print(char_count, contestor, " TRUE")
        return True


def find_marker_or_message(num):
    marker_list = [e for e in _INPUT[:num]]
    index = num
    if marker_check(marker_list) == True:
        print("Marker Found! ", marker_list, " ::Index: ", index)
        return

    for char in _INPUT[num:]:

        index += 1
        marker_list.pop(0)
        marker_list.append(char)

        if marker_check(marker_list) == True:
            print("Marker Found! ", marker_list, " ::Index: ", index)
            break


# Part 1
find_marker_or_message(4)
# Part 2
find_marker_or_message(14)
