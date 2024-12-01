# -*- coding: utf-8 -*-
"""
Created on Dec 01 2024

Last major update on Dec 01 2024

@author: BERTIN Clément (0lmin)
 
Description:
Advent of Code (AoC) 2024 day 01
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List, Tuple

################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":
    
    # Set file to use as input
    filename: str = "2024/Day01/input.txt"

    # Get file content
    f: StringIO
    with open(filename) as f:
        
        # Read all lines and convert data to int
        lines_values: List[Tuple[int, int]] 
        lines_values = list(map(lambda line: list(map(int, line.replace("\n", "").split("   "))), 
                                f.readlines()))
        
        # Split data in two lists and sort them
        left: List[int]
        right: List[int]
        left, right = map(sorted, map(list,zip(*lines_values)))
        
        # Compute the sum of the list diff
        result_p1: int = sum([abs(l - r) for r, l in zip(left, right)])
        
        # Compute the similarity score of the list
        result_p2: int = sum([l * right.count(l) for l in left])
        
        # Print the results
        print(f"{result_p1 = }")
        print(f"{result_p2 = }")