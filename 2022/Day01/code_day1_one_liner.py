# -*- coding: utf-8 -*-
"""
Created on Dec 01 2022

Last major update on Nov 30 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 1's challenge of the Advent of Code (AoC) made as a one-liner
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
        
    # One liner to parse the list of lines and get the result
    print("result_p1 =", int(max([sum(list(map(float, lines_list[([-1] + list(map(lambda x: x[0], filter(lambda x: x[1].startswith('\n'), enumerate(lines_list)))))[i] + 1:
                                            ([-1] + list(map(lambda x: x[0], filter(lambda x: x[1].startswith('\n'), enumerate(lines_list)))))[i+1]]))) 
                                                    for i in range(len([-1] + list(map(lambda x: x[0], filter(lambda x: x[1].startswith('\n'), enumerate(lines_list))))) - 1)])))

    print(f"result_p1 =", int(sum(sorted([sum(list(map(float, lines_list[([-1] + list(map(lambda x: x[0], filter(lambda x: x[1].startswith('\n'), enumerate(lines_list)))))[i] + 1:
                                            ([-1] + list(map(lambda x: x[0], filter(lambda x: x[1].startswith('\n'), enumerate(lines_list)))))[i+1]]))) 
                                                    for i in range(len([-1] + list(map(lambda x: x[0], filter(lambda x: x[1].startswith('\n'), enumerate(lines_list))))) - 1)])[-3:])))

