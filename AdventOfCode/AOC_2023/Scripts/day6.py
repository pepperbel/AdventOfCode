# https://adventofcode.com/2023/day/4
# region ---- imports and inputs ----

import re
import AOC_Utilities as utils
import time
start_time = time.time()


INPUT = utils.DataManager(__file__).get_data()
TESTCASES:list[str] = "Time:      7  15   30\nDistance:  9  40  200"


# endregion -------------------------

def parse_input_part_1(input:str):
    time:str = input.split("\n")[0]
    record:str = input.split("\n")[1]
    
    time_split:list[int] = [int(d.strip()) for d in time.split(" ")[1:] if d]
    record_split:list[int] = [int(d.strip()) for d in record.split(" ")[1:] if d]

    return time_split, record_split


def parse_input_part_2(input:str):
    time:str = input.split("\n")[0]
    record:str = input.split("\n")[1]
    
    time_split:list[str] = [d.strip() for d in time.split(" ")[1:] if d]
    record_split:list[str] = [d.strip() for d in record.split(" ")[1:] if d]

    return int("".join(time_split)), int("".join(record_split))


def get_options(time, record):
    distance:int = 0
    hold_times:list[int] = []

    for hold in range(0, time + 1):
        remaining_time:int = time - hold
        distance:int = remaining_time * hold

        if distance > record:
            hold_times.append(hold)
    
    return hold_times


def execute_day_6_part_1(input):
    times, records = parse_input_part_1(input)
    multiplied:int = 1

    for i in range(0, len(times)):
        option_count:int = len(get_options(times[i], records[i]))
        multiplied *= option_count

    return multiplied


def execute_day_6_part_2(input):

    time, record = parse_input_part_2(input)
    option_count:int = len(get_options(time, record))
    
    return option_count


#print("DAY 1 PART 1: ", execute_day_6_part_1(INPUT)) # ANSWER == 840336
print("DAY 1 PART 2: ", execute_day_6_part_2(INPUT)) # ANSWER == 41382569
print("--- %s seconds ---" % (time.time() - start_time))