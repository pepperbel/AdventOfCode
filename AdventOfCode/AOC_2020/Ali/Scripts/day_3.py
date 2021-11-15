import os
import sys


_INPUT_1 =  open(os.path.join(sys.path[0], "../Inputs/input_day_3.txt"), "r")
_INPUT_2 = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
_MAP = []
_OUTPUT_2 = 0
line_length = 0


for line in _INPUT_1:
    line = line.replace("\n", " ")
    line = line.strip()
    _MAP.append(line)
    line_length = len(line)


for coord in _INPUT_2:
    _OUTPUT_1 = 0
    coord_left = 0
    coord_down = 0
    moves_left = coord[0]
    moves_down = coord[1]

    for line_number in range(0, (len(_MAP) - 1)):
        line_array = _MAP[line_number]
        coord_left += moves_left

        try:
            _MAP[coord_down][coord_left] 
        except:
            additive = coord_left - line_length
            coord_left = 0 + additive

        coord_down += moves_down
        
        if coord_down <= (len(_MAP) - 1):
            if _MAP[coord_down][coord_left] == "#":
                _OUTPUT_1 += 1
                print(_OUTPUT_1)

    if _OUTPUT_2 != 0: 
        _OUTPUT_2 *= _OUTPUT_1
    else:
        _OUTPUT_2 = _OUTPUT_1
         
            
print("FIN ", _OUTPUT_1)
print("FIN 2: ", _OUTPUT_2)
    

    
