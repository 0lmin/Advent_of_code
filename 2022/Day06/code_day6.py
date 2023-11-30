# -*- coding: utf-8 -*-
"""
Created on Dec 06 2022

Last major update on Nov 30 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 6's challenge of the Advent of Code (AoC)
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List

################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":
        
    # Set file to use as input
    filename: str = '2022/Day06/input.txt'

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = [line.rstrip() for line in f]
        
        # Initialize results sum
        result_p1: int = 0
        result_p2: int = 0
        
        # Iterate through all lines
        line: str
        for line in lines_list:
            
            # Iterate through the data stream
            starting_index: int
            for starting_index, _ in enumerate(line):
                
                # Check if there is a repeated char using set (4-char buffer)
                if not(result_p1) and len(set(line[starting_index - 4 : starting_index])) == 4:
                    
                    # Set result
                    result_p1 = starting_index
                
                # Check if there is a repeated char using set (14-char buffer)
                if len(set(line[starting_index - 14 : starting_index])) == 14:
                    
                    # Set result
                    result_p2 = starting_index
                    
                # Check for early break (only need p2 because result_p2 >= result_p1)
                if result_p2:
                    break

    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")