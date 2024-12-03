# -*- coding: utf-8 -*-
"""
Created on Dec 03 2024

Last major update on Dec 03 2024

@author: BERTIN Clément (0lmin)
 
Description:
Advent of Code (AoC) 2024 day 03
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

# Define a function to compute the result for a specific string
def compute_result(data: str) -> int:
    """
    Compute the result for the inputted string
    """
    # Split the data by the start string "mul()" (and remove the first one) to get candidates
    candidate_list: List[str] = data.split("mul(")[1:]
    
    # Clean the candidate with the one having ")"
    candidate_list = [candidate.split(")")[0] for candidate in candidate_list if ")" in candidate]
    
    # Check if a "," is in the candidates
    candidate_list = [candidate for candidate in candidate_list if len(candidate.split(",")) == 2]
    
    # Check each side of the candidate and retrieve each needed computation
    computation_list: List[Tuple[int, int]]
    computation_list = [list(map(int, candidate.split(","))) for candidate in candidate_list 
                        if all(map(lambda str: str.isdigit(), candidate.split(",")))]
    
    # Compute the result
    return sum(val[0] * val[1] for val in computation_list)
    

if __name__ == "__main__":
    
    # Set file to use as input
    filename: str = "2024/Day03/input.txt"

    # Get file content
    f: StringIO
    with open(filename) as f:
        
        # Read all lines
        lines_list: List[str] = list(map(lambda line: line.replace("\n", ""), f.readlines()))
        
        # Concatenate line to get a single input to parse
        input_data: str = "".join(lines_list)
        
        # Compute the result of the part 2
        result_p1: int = compute_result(input_data)
        
        # Detect the don't() commands
        processed_data: List[str] = input_data.split("don't()")
        
        # For each substring (excepted the first one) detect if a do() command appear and remove the in between part
        processed_data = [processed_data[0]] + ["".join(data.split("do()")[1:])
                          for data in processed_data[1:] if ("do()" in data)]
        
        # Compute the result of the part 2
        result_p2: int = sum([compute_result(data) for data in processed_data])
        
        # Print results
        print(f"{result_p1 = }")
        print(f"{result_p2 = }")