from multiprocessing.sharedctypes import Value
import os
import sys
import itertools as it
with open(os.path.join(sys.path[0], "../Inputs/input_day_4.txt"), "r") as my_input:
    _INPUT = my_input.read()
    _INPUT = _INPUT.split("\n")
    _BINGO_SUB = _INPUT[0].split(',')
    _BINGO_SUB = [int(x) for x in _BINGO_SUB]
    _INPUT.pop(0)
    _INPUT.pop(0)
    _FIVE_BY_FIVE = []
    _ANSWER_KEYS = []
    five_set = []
    five_keys = []
    for number_set in _INPUT:
        if len(number_set) > 1:
            nums = number_set.split(" ")
            nums = [int(x) for x in nums if x != '']
            for num in nums:
                five_set.append(num)
                five_keys.append(False)
        else:
            _FIVE_BY_FIVE.append(five_set)
            _ANSWER_KEYS.append(five_keys)
            five_keys = []
            five_set = []

print(_FIVE_BY_FIVE)
print(_ANSWER_KEYS)
print(_BINGO_SUB)

PART_ONE = 0
PART_TWO = 0
EXCLUDE_BOARDS = []


def bingo_check(grid_set_index):

    chunks_columns = []
    column_index = [0, 5, 10, 15, 20]
    additive = 0
    # for each loop, we get each column_index + additive and save it as a chunk
    for index in column_index:
        chunks_columns.append([_ANSWER_KEYS[grid_set_index][column_index[0] + additive],
                              _ANSWER_KEYS[grid_set_index][column_index[1] + additive],
                              _ANSWER_KEYS[grid_set_index][column_index[2] + additive],
                              _ANSWER_KEYS[grid_set_index][column_index[3] + additive],
                              _ANSWER_KEYS[grid_set_index][column_index[4] + additive]])
        additive += 1

    # print("columns: %s" % chunks_columns)

    chunk_rows = [_ANSWER_KEYS[grid_set_index][i:i + 5]
                  for i in range(0, len(_ANSWER_KEYS[grid_set_index]), 5)]

    # check rows
    for i in range(0, len(chunk_rows)):
        if False not in chunk_rows[i]:
            #print("BINGO! -- %s" % _FIVE_BY_FIVE[grid_set_index])
            #print("BINGO! -- %s" % _ANSWER_KEYS[grid_set_index])
            #print("ROW: %s" % i)
            _FIVE_BY_FIVE.remove(_FIVE_BY_FIVE[grid_set_index])
            _ANSWER_KEYS.remove(_ANSWER_KEYS[grid_set_index])
            return True
        elif False not in chunks_columns[i]:
            #print("BINGO! -- %s" % _FIVE_BY_FIVE[grid_set_index])
            #print("BINGO! -- %s" % _ANSWER_KEYS[grid_set_index])
            #print("Column: %s" % i)
            _FIVE_BY_FIVE.remove(_FIVE_BY_FIVE[grid_set_index])
            _ANSWER_KEYS.remove(_ANSWER_KEYS[grid_set_index])
            return True
        else:
            return False


def play_bingo():
    # Run through bingo numbers
    for i in range(0, len(_BINGO_SUB)):
        # run through grid sets
        for j, Value in enumerate(reversed(_ANSWER_KEYS)):
            # for j in range(0, len(_ANSWER_KEYS)):

            print("J: %s" % j)
            # print(_FIVE_BY_FIVE)
            print(_ANSWER_KEYS[j])
            print("EXCLUDED %s" % EXCLUDE_BOARDS)
            # if the bingo number is in the grid set
            if _BINGO_SUB[i] in _FIVE_BY_FIVE[j]:
                # get the index of the match
                match_index = _FIVE_BY_FIVE[j].index(_BINGO_SUB[i])
                # set the matching answer key to true
                _ANSWER_KEYS[j][match_index] = True
                print(
                    "bingo num: {} -- match index: {}".format(_BINGO_SUB[i], match_index))

                is_bingo = bingo_check(j)
                bingo_counter = 0
                if is_bingo:
                    bingo_counter += 1
                    added_unmarked = 0
                    temp_list_of_unmarked = []
                    for k in range(0, len(_ANSWER_KEYS[j])):
                        if _ANSWER_KEYS[j][k] == False:
                            temp_list_of_unmarked.append(
                                _FIVE_BY_FIVE[j][k])
                            added_unmarked += _FIVE_BY_FIVE[j][k]
                    print("BINGO! -- %s" % _FIVE_BY_FIVE[j])
                    print("BINGO! -- %s" % _ANSWER_KEYS[j])
                    print("BOARD! -- %s" % j)
                    print("Unmarked: %s" % temp_list_of_unmarked)
                    print("Added unmarked: %s" % added_unmarked)
                    print("BINGO NUM: %s" % _BINGO_SUB[i])

                    if bingo_counter == 1:
                        PART_ONE = added_unmarked * _BINGO_SUB[i]

                    PART_TWO = added_unmarked * _BINGO_SUB[i]


play_bingo()
print("PART ONE RESULT: %s" % PART_ONE)
print("PART ONE RESULT: %s" % PART_TWO)
