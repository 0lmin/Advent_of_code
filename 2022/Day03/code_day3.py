# -*- coding: utf-8 -*-
"""
Created on Dec 03 2022

Last major update on Nov 30 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 3's challenge of the Advent of Code (AoC)
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
    filename: str = '2022/Day03/input.txt'

    # Compute asci value of the bound between lower and upper case
    bound_asci_val: int = ord('a')

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = f.readlines()
        
        # Initialize results sum
        result_p1: int = 0
        result_p2: int = 0
        
        # Iterate through lines for part 1
        line: str
        for line in lines_list:
            first_sack: str = line.replace("\n", "")[(len(line)) // 2:]
            second_sack: str = line.replace("\n", "")[:(len(line)) // 2]
            
            # Check for each char
            char_first_sack: str
            for char_first_sack in first_sack:
                if char_first_sack in second_sack:
                    
                    # Compute its priority
                    if char_first_sack.islower():
                        result_p1 += ord(char_first_sack) - bound_asci_val + 1
                    else:
                        result_p1 += ord(char_first_sack.lower()) - bound_asci_val + 27
                    break
                
        # Iterate through lines for part 2
        iterate_line: int
        for iterate_line in range(0, len(lines_list), 3):
            first_line: str  = lines_list[iterate_line]
            second_line: str = lines_list[iterate_line + 1]
            third_line: str  = lines_list[iterate_line + 2]
            
            # Check for each char
            char_first_sack: str
            for char_first_sack in first_line:
                if char_first_sack in second_line and char_first_sack in third_line:
                    # Compute its priority
                    if char_first_sack.islower():
                        result_p2 += ord(char_first_sack) - bound_asci_val + 1
                    else:
                        result_p2 += ord(char_first_sack.lower()) - bound_asci_val + 27
                    break 
            
    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")