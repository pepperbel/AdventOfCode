import os
import sys
import itertools as it
with open(os.path.join(sys.path[0], "../Inputs/input_day_3.txt"), "r") as my_input:
    _INPUT = my_input.read()
    _INPUT = _INPUT.split("\n")
    #_INPUT = [int(i) for i in _INPUT]
    # print(_INPUT)


def calculate_decimal_from_binary(mylist):
    return_list = []

    for i in range(0, len(mylist)):
        powers_of = len(mylist) - 1
        return_list.append(mylist[i] * pow(2, powers_of - i))

    value = 0

    for i in range(0, len(return_list)):
        value += int(return_list[i])
    return value


def get_most_common_in_collumn(index, mylist, is_one=True):
    list_zeroes = []
    list_ones = []

    for i in range(0, len(mylist)):
        if mylist[i][index] == '0':
            list_zeroes.append(str(mylist[i]))
        else:
            list_ones.append(str(mylist[i]))

    #print("ONE: {}, ZERO: {}".format(list_ones, list_zeroes))
    value = 0 if len(list_zeroes) > len(list_ones) else 1
    #print(len(list_zeroes), len(list_ones), value, index)

    if is_one:
        return list_ones if len(list_ones) >= len(list_zeroes) else list_zeroes
    else:
        return list_zeroes if len(list_zeroes) >= len(list_ones) else list_ones

    # return value, list_zeroes, list_ones


def get_least_common_in_collumn(index, mylist):
    list_zeroes = []
    list_ones = []

    for i in range(0, len(mylist)):
        if mylist[i][index] == '0':
            list_zeroes.append(str(mylist[i]))
        else:
            list_ones.append(str(mylist[i]))


# ---------- Part One ------------ #
gamma = []
epsilon = []

for i in range(0, len(_INPUT[0])):

    zeros = 0
    ones = 0

    for j in range(0, len(_INPUT)):

        if int(_INPUT[j][i]) == 0:
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)

# ---------- Part Two ----------- #

#temp2 = _INPUT
temp2 = ['00100', '11110', '10110', '10111', '10101', '01111',
         '00111', '11100', '10000', '11001', '00010', '01010']

#temp2 = temp
_ZERO = []
_ONE = []


while len(temp2) > 1:
    # print(temp2)

    for i in range(0, len(temp2[0])):
        co2_keep = get_most_common_in_collumn(i, temp2, False)
        o2_keep = get_most_common_in_collumn(i, temp2, True)
        print("TEMP2: {}, ZERO: {}, ONE: {}".format(temp2, co2_keep, o2_keep))
        temp2 = co2_keep if len(co2_keep) > len(o2_keep) else o2_keep

        _ZERO = [int(char) for char in co2_keep[0]]
        _ONE = [int(char) for char in o2_keep[0]]


print(gamma, epsilon, _ZERO, _ONE, calculate_decimal_from_binary(
    _ZERO), calculate_decimal_from_binary(_ONE))

print("PART ONE ---------- Gamma: {}, Epsilon: {} , POWER_CONSUMPTION: {}".format(gamma, epsilon,
                                                                                  calculate_decimal_from_binary(gamma) * calculate_decimal_from_binary(epsilon)))
print("PART TWO ---------- ZERO: {}, ONE: {} , POWER_CONSUMPTION: {}".format(_ZERO, _ONE,
                                                                             calculate_decimal_from_binary(_ZERO) * calculate_decimal_from_binary(_ONE)))
