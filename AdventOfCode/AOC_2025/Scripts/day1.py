import os
import sys
import enum

def interpret_input(input:str):
    input_direction = input[0]
    input_distance = int(input[1:])

    return [input_direction, input_distance]

with open(os.path.join(sys.path[0], "../Inputs/input_day1.txt"), "r") as my_input:
    _INPUT:list[str] = my_input.read().splitlines()
    _INPUT:list = [interpret_input(i) for i in _INPUT if i]
    #print(_INPUT)

TEST_INPUT = [
    ["L", 68],
    ["L", 30],
    ["R", 48],
    ["L", 5],
    ["R", 60],
    ["L", 55],
    ["L", 1],
    ["L", 99],
    ["R", 14],
    ["L", 182]
]

starting_dial = 50


def get_password(input, current_dial, dbg=False):
    zero_counter_part_1 = 0
    zero_counter_part_2 = 0

    for direction, rotation in input:
        step = 1 if direction == "R" else -1

        if dbg:
            print(f" ===== START ROUND: direction:{step}, rotation:{rotation}, current dial:{current_dial} ===")
            print(f"Current Dial at start: {current_dial}")

        for unit in range(rotation):
            current_dial = (current_dial + step) % 100

            if dbg:
                print(f"Current Dial after instruction: {current_dial}")

            if current_dial == 0:
                zero_counter_part_2 += 1
                if dbg:
                    print(f"Zero Coutner part 2 incremented: {zero_counter_part_2}")
        
        if current_dial == 0:
            zero_counter_part_1 += 1
            if dbg:
                print(f"Zero Coutner part 1 incremented: {zero_counter_part_2}")


    return zero_counter_part_1, zero_counter_part_2

password_part_1, password_part_2 = get_password(input=_INPUT, current_dial=starting_dial, dbg=False)
#password_part_1, password_part_2 = get_password(input=TEST_INPUT, current_dial=starting_dial, dbg=True)

print("FINAL PASSWORD PART 1: ", password_part_1) # 1180
print("FINAL PASSWORD PART 2: ", password_part_2) # 6892


