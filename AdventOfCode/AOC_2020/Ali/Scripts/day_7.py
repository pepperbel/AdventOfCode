import os
import sys
import math
with open(os.path.join(sys.path[0], "../Inputs/input_day_7.txt"), "r") as my_input:
    """
    Line Example: dark cyan bags contain 2 wavy beige bags.
    - remove the "."
    - strip " bags" and " bag"
    -
    """
    _INPUT_1 = my_input.read().replace(".", "")
    _INPUT_1 = _INPUT_1.replace(" bags", "").replace(" bag", "").split("\n")
    _INPUT_1 = [i.split(" contain ") for i in _INPUT_1]


class BAG(object):
    """Creates a BAG object that has properties
    for _name_, _contents_ an wether or not it directly contains
    a shiny gold bag
    """

    def __init__(self, data):
        self._bag_name = data[0]
        self._directly_contains_shiny_gold = self._find_shiny_gold(data[1])
        self._indirectly_contains_shiny_gold = False
        self._contents = self._populate_content_dict(data[1])

    @property
    def name(self):
        return self._bag_name

    @property
    def has_shiny_gold_direct(self):
        return self._directly_contains_shiny_gold

    @property
    def has_shiny_gold_indirect(self):
        return self._indirectly_contains_shiny_gold

    @has_shiny_gold_indirect.setter
    def has_shiny_gold_indirect(self, value):
        self._indirectly_contains_shiny_gold = value

    @property
    def contents(self):
        return self._contents

    def _find_shiny_gold(self, raw_data):
        """will return TRUE if the bag contains shiny gold
        Args:
            raw_data (string): contents of bag
        Returns:
            bool: shiny gold
        """
        if "shiny gold" in raw_data:
            return True
        else:
            return False

    def _populate_content_dict(self, raw_data):
        """Orders contents into a dict object
        Args:
            raw_data (string): bag contents
        Returns:
            dict: bag contents
        """
        if "no other" in raw_data:
            return None

        data_dict = {}

        if ',' in raw_data:
            raw_data_list = raw_data.split(", ")
            # print(raw_data_list)
            for set in raw_data_list:
                set_list = set.split(" ")
                # print(set_list)
                data_dict.update({"{} {}".format(
                    set_list[1], set_list[2]): int(set_list[0])})
        else:
            data_list = raw_data.split(" ")
            # print(data_list)
            data_dict.update({"{} {}".format(
                data_list[1], data_list[2]): int(data_list[0])})

        return data_dict


class BAG_MANAGER(object):

    def __init__(self, data):
        self._DATABASE = data
        self._DIRECT_CONTAINERS = []
        self._BAG_DICT = {}

        for i in range(0, len(self._DATABASE)):
            bag = BAG(self._DATABASE[i])
            self._BAG_DICT.update({bag.name: bag})
            if bag.has_shiny_gold_direct:
                self._DIRECT_CONTAINERS.append(bag.name)

    def _check_contents(self, input_list, output_list):
        for bag_name, bag in self._BAG_DICT.items():
            for input_bag in input_list:

                if bag.contents != None and input_bag in bag.contents:
                    bag.has_shiny_gold_indirect = True
                    output_list.append(bag.name)
                    # break

    def part_one(self):

        indirect_container_lists = [self._DIRECT_CONTAINERS]

        harvest = True
        id = 0

        while harvest:
            new_list = []
            self._check_contents(indirect_container_lists[id], new_list)

            if new_list:
                indirect_container_lists.append(new_list)
                id += 1
                harvest = True
            else:
                harvest = False

        counter = 0
        for bag_name, bag in self._BAG_DICT.items():
            if bag.has_shiny_gold_direct or bag.has_shiny_gold_indirect:
                counter += 1

        print("PART ONE: {}".format(counter))

    def part_two(self):

        bag_counter = 0
        current_bags = [self._BAG_DICT["shiny gold"]]

        while len(current_bags) > 0:
            # print(current_bags)
            curr_bag = current_bags.pop()
            if curr_bag.contents != None:
                bag_counter += 1
                for bag, count in curr_bag.contents.items():
                    for i in range(count):
                        current_bags.append(self._BAG_DICT[bag])
                        #print(curr_bag.name, curr_bag.contents, bag)
            # else:
                #print(curr_bag.name, curr_bag.contents)

        print("INCOMPLETE: {}".format(bag_counter))


day_7 = BAG_MANAGER(_INPUT_1)
day_7.part_one()
day_7.part_two()
