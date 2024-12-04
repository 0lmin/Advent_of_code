# -*- coding: utf-8 -*-
"""
Created on Dec 04 2024

Last major update on Dec 04 2024

@author: BERTIN Clément (0lmin)
 
Description:
Advent of Code (AoC) 2024 day 04
"""

################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":
    
    # Set file to use as input
    filename: str = "2024/Day04/input.txt"
    
    # Retrieve the input data as a single str
    input_data: str = open(filename).read()
    
    # Get the length of one line 
    line_size: int = len(input_data.split("\n")) + 1
    
    # Compute the result for part 1
    result_p1: int = sum([sum(input_data[i - 1::1][:4]  in ["XMAS", "SAMX"] for i in range(len(input_data))),
                          sum(input_data[i - line_size - 1::line_size-1][:4]  in ["XMAS", "SAMX"] for i in range(len(input_data))),
                          sum(input_data[i - line_size::line_size][:4]  in ["XMAS", "SAMX"] for i in range(len(input_data))),
                          sum(input_data[i - line_size + 1::line_size+1][:4]  in ["XMAS", "SAMX"] for i in range(len(input_data)))])
    
    # Compute the result for part 2
    result_p2: int = sum([all(input_data[i - size::size][:3] in ["MAS", "SAM"] 
                              for size in (line_size - 1, line_size + 1)) 
                            for i in range(len(input_data))])
    
    
    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")