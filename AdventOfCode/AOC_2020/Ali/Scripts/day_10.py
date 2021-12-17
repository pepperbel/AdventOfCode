from collections import Counter
import os
import sys
with open(os.path.join(sys.path[0], "../Inputs/input_day_10.txt"), "r") as my_input:
    _INPUT = my_input.read().split("\n")
    _INPUT = sorted([int(i) for i in _INPUT])
    _ADAPTERS = [0] + _INPUT + [_INPUT[-1] + 3]
    # print(_ADAPTERS)

# -------- PART ONE -------- #
jolts_diff = [_ADAPTERS[n] - _ADAPTERS[n-1]
              for n in range(1, len(_ADAPTERS))]
diff_dict = dict(Counter(jolts_diff))
product = diff_dict[1] * diff_dict[3]


# -------- PART TWO -------- #
jolts = _INPUT + [_INPUT[-1] + 3]
counter = {0: 1}
for adapter in jolts:
    counter[adapter] = counter.get(
        adapter - 3, 0) + counter.get(adapter - 2, 0) + counter.get(adapter - 1, 0)


print("PART ONE: {}".format(product))
print("PART TWO: {}".format(counter[jolts[-1]]))


def old_part_one():
    # -------- PART ONE -------- #
    #current_adapter = 0
    #one_jolt = 0
    #three_jolts = 0

    #list_of_possible_arrangements = []
    #current_arrangement = []

    # for jolt in _INPUT:
    #     if jolt == _INPUT[-1]:
    #         three_jolts += 1
    #         current_arrangement.append(3)
    #         list_of_possible_arrangements.append(current_arrangement)
    #         print("Part one: {}".format(one_jolt * three_jolts))
    #         break

    #     if jolt - current_adapter == 3:
    #         three_jolts += 1
    #         current_adapter = jolt
    #         current_arrangement.append(3)

    #     if jolt - current_adapter == 1:
    #         one_jolt += 1
    #         current_adapter = jolt
    #         current_arrangement.append(1)
    pass


print(map(lambda x: 9 + (1 if x == 3 else 6), range(4)))
