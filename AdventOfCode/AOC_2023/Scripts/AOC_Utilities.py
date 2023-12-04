import os
import sys

#AOC_Utilities.DataManager(__file__).get_data()


class DataManager(object):

    def __init__(self, file:str, debug:bool=False):
        self.filename:str = os.path.basename(file)
        self.name:str = self.filename[:-3]
        self.input_file:str = os.path.join("Inputs", "input_{}.txt".format(self.name))

        # region  --- DEBUG ---
        if debug:
            print("Utils Filename: ", self.filename)
            print("Utils Name: ", self.name)
            print("Utils Input File: ", self.input_file)
            

        # endregion -----------
    
    def get_data(self, splitlines:bool=False):
        with open(os.path.join(sys.path[0].replace("Scripts", ""), self.input_file), "r") as my_input:
            _input:str = my_input.read()
            if splitlines:
                _input:list[str] = _input.split("\n")
        
        return _input
