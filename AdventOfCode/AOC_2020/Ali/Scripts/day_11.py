import os
import sys
from collections import Counter
with open(os.path.join(sys.path[0], "../Inputs/input_day_11.txt"), "r") as my_input:
    _INPUT_1 = my_input.read().split("\n")
    # print(_INPUT_1)


class Map:
    def __init__(self, input):
        self._COORDINATE_MAP = self.__create_map__(input)
        self._temp_new_map = {}
        self._MAX_COLUMN = (len(input) - 1)
        self._MAX_ROW = len(input[0]) - 1

    def __create_map__(self, map_input):
        """[summary]

        Args:
            map_input ([list]): [lines of symbols to be converted to coords]

        Returns:
            [dict]: [keys are coords, values are symbols]
        """
        map = {}

        for row_index in range(0, len(map_input)):
            for column_index in range(0, len(map_input[row_index])):
                map[(column_index, row_index)
                    ] = map_input[row_index][column_index]
        return map

    def _get_adjacent_seats_(self, coord):
        """[returns clockwise adjacent coordinates of --coord--]

        Args:
            coord ([tuple]): [coordinate in map]

        Returns:
            [List]: [N, NE, E, SE, S, SW, W, NW]
        """
        x = coord[0]
        y = coord[1]
        return [(x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1)]

    def _rule_on_empty_seat_(self, seat_coord):
        empty_seats_count = 0  # must be 8
        for seat in self._get_adjacent_seats_(seat_coord):
            if seat[0] >= 0 and seat[0] <= self._MAX_ROW and seat[1] >= 0 and seat[1] <= self._MAX_COLUMN:
                if self._COORDINATE_MAP[seat] == "L" or self._COORDINATE_MAP[seat] == ".":
                    empty_seats_count += 1
            else:
                empty_seats_count += 1

        if empty_seats_count == 8:
            self._temp_new_map[seat_coord] = "#"

    def _rule_on_occupied_seat_(self, seat_coord):
        occupied_seats_count = 0  # must be 4 or more
        for seat in self._get_adjacent_seats_(seat_coord):
            if seat[0] >= 0 and seat[0] <= self._MAX_ROW and seat[1] >= 0 and seat[1] <= self._MAX_COLUMN:
                if self._COORDINATE_MAP[seat] == "#":
                    occupied_seats_count += 1

        if occupied_seats_count >= 4:
            self._temp_new_map[seat_coord] = "L"

    def run_seat_shuffle(self):
        for coordinate in self._COORDINATE_MAP:
            self._temp_new_map[coordinate] = self._COORDINATE_MAP[coordinate]

            if self._COORDINATE_MAP[coordinate] == "L":
                self._rule_on_empty_seat_(coordinate)
            elif self._COORDINATE_MAP[coordinate] == "#":
                self._rule_on_occupied_seat_(coordinate)
            elif self._COORDINATE_MAP[coordinate] == ".":
                self._temp_new_map[coordinate] == "."

        self._COORDINATE_MAP = self._temp_new_map
        self._temp_new_map = {}
        counted = dict(Counter(self._COORDINATE_MAP.values()))
        return counted["#"]


my_map = Map(_INPUT_1)
_OUTPUT_1 = 0  # 2334

while True:
    if _OUTPUT_1 == my_map.run_seat_shuffle():
        print("We done here", _OUTPUT_1)
        break

    _OUTPUT_1 = my_map.run_seat_shuffle()
