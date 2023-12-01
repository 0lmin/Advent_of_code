# -*- coding: utf-8 -*-
"""
Created on Dec 01 2023

Last major update on Dec 01 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 1's challenge of the Advent of Code (AoC) 2023
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List, Dict

# Import deepcopy utils
from copy import deepcopy

################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":
    
    # Set file to use as input
    filename: str = '2023/Day01/input.txt'
    
    # Initialize results
    result_p1: int = 0
    result_p2: int = 0
    
    # Set the correspondence dictionary for string number to numeric value
    correspondence_dict: Dict[str, str] = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = list(map(lambda line: line.replace("\n", ""), f.readlines()))
        
        # Iterate through lines
        line: str
        for line in lines_list:
            
            # Part 1
            # Remove all non numeric char in the line
            numeric_line: str = [char for char in line if char.isnumeric()]
            
            # Keep only the first and last number
            current_value: int = int(f"{numeric_line[0]}{numeric_line[-1]}")
            
            # Add the current value to the result
            result_p1 += current_value
            
            # Part 2
            # Initialize the converted line
            converted_line: str = deepcopy(line)
                
            # Iterate through each number string value
            str_num: str
            num_val: int
            for str_num, num_val in correspondence_dict.items():
                
                # Replace number str value if it exists
                converted_line = converted_line.replace(str_num, f"{num_val}")             
                        
            # Remove all non numeric char in the line
            numeric_line: str = [char for char in converted_line if char.isnumeric()]
            
            # Keep only the first and last number
            current_value: int = int(f"{numeric_line[0]}{numeric_line[-1]}")
            
            # Add the current value to the result
            result_p2 += current_value
            
    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")