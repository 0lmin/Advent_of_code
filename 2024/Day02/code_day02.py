# -*- coding: utf-8 -*-
"""
Created on Dec 03 2024

Last major update on Dec 03 2024

@author: BERTIN Clément (0lmin)
 
Description:
Advent of Code (AoC) 2024 day 02
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

# Define a function to check if a report is safe
def is_safe(report: List[int]) -> int:
    """
    Return -1 if the report is safe, else return the index 
    where failure has been found
    """
    
    # Check if levels are decreasing
    if report[1] < report[0]:
        
        # Convert to equivalent increasing report
        report = [level * -1 for level in report]
        
    # Iterate through report
    iterate_level: int
    for iterate_level in range(len(report) - 1):
        
        # Compute direct diff
        diff: int = report[iterate_level + 1] - report[iterate_level]
        
        # Check if an issue occur
        if diff > 3 or diff < 1:

            # The report is unsafe
            return iterate_level
        
    # The report is safe
    return -1

if __name__ == "__main__":
    
    # Set file to use as input
    filename: str = "2024/Day02/input.txt"

    # Get file content
    f: StringIO
    with open(filename) as f:
        
        # Read all lines and format them as list of int
        lines_list: List[List[int]]
        lines_list = list(map(lambda line: list(map(int, line.replace("\n", "").split(" "))), 
                              f.readlines()))
        
        # Initialize the count of safe reports in part 1
        result_p1: int = 0
        
        # Initialize the count of safe reports in part 2
        result_p2: int = 0
                
        # Iterate through all reports
        report: List[int]
        for report in lines_list:
            
            # Retrieve the check status of safety
            is_safe_status: int = is_safe(report)
            
            # Check if the report is safe
            if is_safe_status == -1:
                
                # Increase the count of safe report fort part 1 and 2
                result_p1 += 1
                result_p2 += 1                
                
            # Handle the possible error case
            else:
                
                # Handle the specific case of second element issue inducing wrong monotonicity direction
                # The first case is checked only for a specific case of wrong monotonicity direction detection
                if is_safe(report[:is_safe_status - 1] + report[is_safe_status:]) == -1 or \
                   is_safe(report[:is_safe_status] + report[is_safe_status + 1:]) == -1 or \
                   is_safe(report[:is_safe_status + 1] + report[is_safe_status + 2:]) == -1:
                
                    # Increase the count of safe report for part 2
                    result_p2 += 1
                    
        # Print results
        print(f"{result_p1 = }")
        print(f"{result_p2 = }")