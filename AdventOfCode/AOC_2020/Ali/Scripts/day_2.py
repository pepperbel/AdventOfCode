import os
import sys
import re

_INPUT =  open(os.path.join(sys.path[0], "../Inputs/input_day_2.txt"), "r")
_OUTPUT_1 = 0
_OUTPUT_2 = 0


def how_luz_gets_password_sets(line):

    '''
    Every parenthesis is a group. 
    (/d) is any 1 number, with the +, is any numbers. 
    then in between parenthesis the "-" is the separator of the range, so the first part is :
    (any amount of numbers before a dash) (any amount of numbers after the dash and before a space)
    then (.) is any 1 character, 
    so the next parenthesis is (any character after a space and before the colon)
    and last if you add the + is any number of characters, so the last parenthesis is 
    (any number of characters after a colon)
    (numbers)-(numbers) (1 char):(characters)
    '''

    valid_passwords = 0

    password_set = re.search(r"(\d+)-(\d+) (.): (.+)", line)
    range_begin = int(password_set.group(1))
    range_end = int(password_set.group(2))
    key_letter = password_set.group(3)
    password = password_set.group(4)

    if range_begin <= password.count(key_letter) <= range_end:
        valid_passwords += 1

    print("First part: ", valid_passwords)
    #print(password_set)
    #return password_set


def get_password_set(line):

    ''' Returns a password_set array
        []
    '''
    line_password_set = []
    password = line.split(": ")
    letter = password[0].split(" ")
    number_range = letter[0].split("-")
    password = password[1].replace("\n", " ")
    password = password.strip()

    line_password_set.append(int(number_range[0]))
    line_password_set.append(int(number_range[1]))
    line_password_set.append(letter[1])
    line_password_set.append(password)
    return line_password_set


for line in _INPUT:
    password_set = get_password_set(line)
    number_of_occurances = 0

    #--------DAY 2 part 1----------#
    for letter in password_set[3]:
        if letter is password_set[2]:
            number_of_occurances += 1
    
    if number_of_occurances >= password_set[0] and number_of_occurances <= password_set[1]:
        _OUTPUT_1 += 1
    #------------------------------#
    #--------DAY 2 part 2----------#
    password = password_set[3]

    if password[(password_set[0] - 1)] is password_set[2] or password[(password_set[1] - 1)] is password_set[2]:
        if password[(password_set[0] - 1)] is password_set[2] and password[(password_set[1] - 1)] is password_set[2]:
            continue
        else:
            _OUTPUT_2 += 1        
    #------------------------------#

print("Part 1: ", _OUTPUT_1)
print("Part 2: ", _OUTPUT_2)