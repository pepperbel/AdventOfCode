import os
import sys
import enum

def split_range_id(id):
    first_id = int(id.split("-")[0])
    second_id = int(id.split("-")[1])

    return [first_id, second_id]


with open(os.path.join(sys.path[0], "../Inputs/input_day2.txt"), "r") as my_input:
    _INPUT:str = my_input.read()
    _INPUT:list[str] = _INPUT.split(",")
    _INPUT:list = [split_range_id(i) for i in _INPUT if i]
    #print(_INPUT)

test_input = [
    [11, 22],
    [95, 115],
    [998,1012],
    [1188511880,1188511890],
    [222220,222224],
    [1698522,1698528],
    [446443,446449],
    [38593856,38593862]
]

def cut_string_compare(str_num, n):
    if len(str_num) % n != 0:
        return False

    size = len(str_num) // n
    parts = [str_num[i:i+size] for i in range(0, len(str_num), size)]
    return (len(set(parts)) == 1)

def dissect_those_mofo_ranges(input, dbg=False):
    invalid_add_counter_part_1 = 0
    invalid_add_counter_part_2 = 0

    for id_pair in input:
        if dbg:
            print("======= START ==========")
            print(id_pair)

        for i in range(id_pair[0], id_pair[1] + 1):
            if dbg:
                print(i)
            if str(i).startswith("0"):
                # INVALID ID
                invalid_add_counter += i
                invalid_add_counter_part_2 += i
                continue

            if cut_string_compare(str(i), n=2):
                # INVALID ID
                invalid_add_counter_part_1 += i
                invalid_add_counter_part_2 += i
                continue
            if cut_string_compare(str(i), n=3):
                invalid_add_counter_part_2 += i
                continue
            if cut_string_compare(str(i), n=5):
                invalid_add_counter_part_2 += i
                continue
            if cut_string_compare(str(i), n=7):
                invalid_add_counter_part_2 += i
                continue
    
    return invalid_add_counter_part_1, invalid_add_counter_part_2

#invalid_ids_part_1 = dissect_those_mofo_ranges(test_input, dbg=True)
invalid_ids_part_1, invalid_ids_part_2 = dissect_those_mofo_ranges(_INPUT, dbg=False) 
print("PART 1: ", invalid_ids_part_1) #52316131093
print("PART 2: ", invalid_ids_part_2) #69564213293

