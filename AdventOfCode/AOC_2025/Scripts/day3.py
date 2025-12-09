import os
import sys
import enum

with open(os.path.join(sys.path[0], "../Inputs/input_day3.txt"), "r") as my_input:
    _INPUT:str = my_input.read().splitlines()
    #print(_INPUT)

test_input = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
]

def get_highest_number(bank, n):
    highest_number = 0
    while n > 0:
        print("N:", n)
        if n == 1:
            max_search = 1
        else:
            max_search = len(bank) - (n-1)
        print(len(bank), n, max_search, bank[max_search:], bank[:max_search], bank[max_search])

        for i in range(len(bank)):
            if bank[i] == bank[max_search]:
                continue
            val = int(bank[i]) * (10 ** (n-1))
            if len(str(val)) == len(str(highest_number)):
                added_val = val
            else:
                added_val = highest_number + val
            print(added_val)
            #print("VAL: ", val)
            if added_val > highest_number:
                highest_number = added_val
                print("HIGHEST:", highest_number)
        
        n -= 1


def get_bank_joltage(bank:str, dbg:bool=False) -> int:

    digits = [int(ch) for ch in bank.strip()]
    n = len(digits)

    highest_number = -1

    for i in range(n):
        for j in range(i + 1, n):
            val = digits[i] * 10 + digits[j]
            if val > highest_number:
                highest_number = val
                if dbg:
                    highest_pair = (digits[i], digits[j])

    if dbg:
        print(f"BANK {bank}, Highest Num: {highest_number} (pair {highest_pair[0]}{highest_pair[1]})")

    return highest_number

def get_total_output(bank_list:list[str], dbg:bool=False) -> int:
    total_joltage:int = 0

    for bank in bank_list:
        if not bank.strip():
            continue
        total_joltage += get_bank_joltage(bank, dbg=dbg)

    return total_joltage

#joltage_part_1 = get_total_output(_INPUT, dbg=False) 
#joltage_part_1 = get_total_output(test_input, dbg=True) 
#print("PART 1: ", joltage_part_1) #17155
#print("PART 2: ", joltage_part_2) #



#get_highest_number("234234234234278", 12)
get_highest_number("987654321111111", 12)