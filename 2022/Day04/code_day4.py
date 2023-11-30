# -*- coding: utf-8 -*-
"""
Created on Dec 04 2022

Last major update on Nov 30 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 4's challenge of the Advent of Code (AoC)
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
    filename: str = '2022/Day04/input.txt'

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = [line.rstrip() for line in f]
        
        # Initialize results sum
        result_p1: int = 0
        result_p2: int = 0
        
        # Iterate through lines for part 1
        line: str
        for line in lines_list:
            
            # Get each elf section assignment
            elf1: List[int] # Size 2
            elf2: List[int] # Size 2
            elf1, elf2 = list(map(lambda x: list(map(int, x.split('-'))), line.split(",")))
            
            # Detect if a section is encapsulated inside the other
            if ((elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or
                (elf2[0] >= elf1[0] and elf2[1] <= elf1[1])):
                result_p1 += 1
                
            # Detect overlapping sections
            if not((elf1[1] < elf2[0]) or (elf2[1] < elf1[0])):
                result_p2 += 1

    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")