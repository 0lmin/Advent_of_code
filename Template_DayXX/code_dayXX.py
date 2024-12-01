# -*- coding: utf-8 -*-
"""
Created on XXX XX XXXX

Last major update on XXX XX XXXX

@author: BERTIN Clément (0lmin)
 
Description:
Advent of Code (AoC) 20XX day XX
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
    filename: str = "20XX/DayXX/input.txt"

    # Get file content
    f: StringIO
    with open(filename) as f:
        
        # Read all lines
        lines_list: List[str] = list(map(lambda line: line.replace("\n", ""), f.readlines()))
