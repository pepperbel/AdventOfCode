import os
import sys


with open(os.path.join(sys.path[0], "../Inputs/input_day4.txt"), "r") as my_input:
    _INPUT:str = my_input.read()
    _INPUT:list[str] = _INPUT.split("\n")
    #print(_INPUT)

test_input = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]

def search_adjacent_tiles(i, row, above_row=None, below_row=None, dbg=False):
    adjacent_coutner = 0

    if dbg:
        print("INDEX: ", i)
        print("ROW:", row)
        print("ABOVE ROW:", above_row)
        print("BELOW ROW:", below_row)

    if i != 0:
        if row[i-1] == "@":
            adjacent_coutner += 1
        if above_row != None and above_row[i-1] == "@":
            adjacent_coutner += 1
        if  below_row != None and below_row[i-1] == "@":
            adjacent_coutner += 1
    if i != len(row) - 1:
        if row[i+1] == "@":
            adjacent_coutner += 1
        if above_row != None and above_row[i+1] == "@":
            adjacent_coutner += 1
        if  below_row != None and below_row[i+1] == "@":
            adjacent_coutner += 1

    if  above_row != None and above_row[i] == "@":
        adjacent_coutner += 1

    if  below_row != None and below_row[i] == "@":
        adjacent_coutner += 1

    return True if adjacent_coutner < 4 else False

def find_accessible_rows(input, dbg=False):
    total_rolls:int = 0
    remove_map:list = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "@":
                if i == 0:
                    remove = search_adjacent_tiles(j, row=input[i], below_row=input[i+1], dbg=dbg)
                elif i == len(input[i]) - 1:
                    remove = search_adjacent_tiles(j, row=input[i], above_row=input[i-1], dbg=dbg)
                else:
                    remove = search_adjacent_tiles(j, row=input[i], above_row=input[i-1], below_row=input[i+1], dbg=dbg)

                if remove:
                    total_rolls += 1
                    remove_map.append([i, j])

    return total_rolls, remove_map

def replace_removed(input, map):
    for coord in map:
        i = coord[0]
        j = coord[1]

        if input[i][j] == "@":
            input[i] = input[i][:j] + "x" + input[i][j+1:]

    return input

def iterate_until_all_removed(input, dbg=False):
    final_rolls = 0
    final_rolls, map = find_accessible_rows(input, dbg=dbg)
    input = replace_removed(input, map, dbg=dbg) 

    while len(map) > 0:
        rolls, map = find_accessible_rows(input, dbg=dbg)
        input = replace_removed(input, map) 

        final_rolls += rolls

    return final_rolls


part_1 = find_accessible_rows(_INPUT, dbg=False)
part_2 = iterate_until_all_removed(_INPUT, dbg=False)
print(f"Part 1: Removed a total roll count of: {part_1}") #1411
print(f"Part 2: Removed a total roll count of: {part_2}") #8557
