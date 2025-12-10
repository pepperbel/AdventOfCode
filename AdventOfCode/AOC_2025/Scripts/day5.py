import os
import sys

with open(os.path.join(sys.path[0], "../Inputs/input_day5.txt"), "r") as my_input:
    _INPUT:str = my_input.read()
    _INPUT:list[str] = _INPUT.split("\n\n")
    _INPUT[0] = _INPUT[0].split("\n")
    _INPUT[1] = _INPUT[1].split("\n")
    # print(_INPUT)
    # print(len(_INPUT))


test_input = [
    [
        "3-5",
        "10-14",
        "16-20",
        "12-18"
    ],[
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]
]

def merge_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda r:r[0])
    merged = []
    current_start, current_end = sorted_ranges[0]

    for start, end in sorted_ranges[1:]:
        should_merge = start <= current_end + 1
        if should_merge:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    
    merged.append((current_start, current_end))
    return merged

def get_all_fresh_ids(ranges):
    merged_ranges = merge_ranges(ranges)
    counter = 0
    for r in merged_ranges:
        number = (r[1] + 1) - r[0]
        counter += number

    return counter

def parse_ranges(range_strs):
    ranges = []
    for r in range_strs:
        start_str, end_str = r.split("-")
        start = int(start_str)
        end = int(end_str)
        ranges.append((start, end))
    #print("RANGES:", ranges)
    return ranges

def find_in_ranges(ranges, id):
    for r in ranges:
        if id >= r[0] and id <= r[1]:
            #print("FRESH AS FUCK!")
            return True

    return False

def find_fresh_ingredients(range_list, ids=None):

    if ids == None:
        total_fresh_range_count = get_all_fresh_ids(range_list)

        return total_fresh_range_count
    
    else:
        fresh_ingredients_counter = 0
        ids = [int(i) for i in ids]
        for id in ids:
            if find_in_ranges(range_list, id):
                fresh_ingredients_counter += 1
    
        return fresh_ingredients_counter

# test_ranges = parse_ranges(test_input[0])
# test_1 = find_fresh_ingredients(test_ranges, test_input[1])
# test_2 = find_fresh_ingredients(test_ranges)
# print("TEST OUTPUT 1: ", test_1)
# print("TEST OUTPUT 2: ", test_2)

range_list = parse_ranges(_INPUT[0])
part_1 = find_fresh_ingredients(range_list=range_list, ids=_INPUT[1])
part_2 = find_fresh_ingredients(range_list=range_list)
print(f"PART 1, FRESH INGREDIENTS: {part_1}") #865
print(f"PART 2, FRESH INGREDIENTS: {part_2}") #352556672963116