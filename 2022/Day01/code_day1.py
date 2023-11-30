# -*- coding: utf-8 -*-
"""
Created on Dec 01 2022

Last major update on Nov 30 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 1's challenge of the Advent of Code (AoC)
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
    filename: str = '2022/Day01/input.txt'

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = f.readlines()
        
        # Initialize list of elves carry
        elves_carry_list: List[int] = [0]
        
        # Iterate through lines
        line: str
        for line in lines_list:
            
            # Create a new elves
            if line == '\n':
                elves_carry_list.append(0)
                
            # Add new carry for current elves
            else:
                elves_carry_list[-1] += float(line)
            
        # Get results
        result_p1: int = int(max(elves_carry_list))
        result_p2: float = int(sum(sorted(elves_carry_list)[-3:]))
        
    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")