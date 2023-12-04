# -*- coding: utf-8 -*-
"""
Created on Dec 04 2023

Last major update on Dec 04 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 3's challenge of the Advent of Code (AoC) 2023
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List, Set, Tuple, Dict

# Import re for regexp utils
import re

################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":
    
    # Set file to use as input
    filename: str = '2023/Day03/input.txt'
    
    # Initialize results
    result_p1: int = 0
    result_p2: int = 0
    
    # Initialize the dictionary of all numbers and their neighbors possible positions
    number_dict: Dict[Tuple[int, Tuple[int, int]], List[Tuple[int, int]]] = dict()
    
    # Initialize the set of all operators' position
    operator_position_set: Set[Tuple[int, int]] = set()
    
    # Initialize the set of all gear' position
    gear_position_set: Set[Tuple[int, int]] = set()
    
    # Initialize the gear association count dict
    gear_association_dict: Dict[Tuple[int, int], List[int]] = dict()

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = list(map(lambda line: line.replace("\n", ""), f.readlines()))
                    
        # Iterate through lines to find numbers
        iterate_line: int
        line: str
        for iterate_line, line in enumerate(lines_list):
            
            # Get all content
            content_list: List[str] = [val for val in '.'.join(re.split(r'(\d+)', line)).split(".") if val != ""]
            
            # Initialize the start position of  numbers to search if there is another occurrence of the same number in the line
            number_position: Tuple[int, int] = (-1, -1)
    
            # Initialize the position of operator to search if there is another occurrence of the same number in the line
            operator_position: Tuple[int, int] = (-1, -1)
            
            # Initialize the position of operator to search if there is another occurrence of the same number in the line
            gear_position: Tuple[int, int] = (-1, -1)
            
            # Initialize the number str to save
            number: str = ''
            
            # Initialize the operator str to save
            operator: str = ''
            
            # Initialize the gear str to save
            gear: str = ''
            
            # Iterate through all content of the map
            content: str
            for content in content_list:
                
                # Check if the content is a number
                if content.isnumeric():
                    
                    # Handle when same number are on the same line
                    if number_position[1] == iterate_line:
                                        
                        # Get the start position of the number
                        number_position = (number_position[0] + len(number) + line[number_position[0] + len(number):].find(content), iterate_line)
                    
                    # Handle the generic case
                    else:
                        
                        # Get the start position of the number
                        number_position = (line.find(content), iterate_line)
                    
                    # Get the neighbors possible position
                    neighbors_possible_position: List[Tuple[int, int]] = (
                        [(pos_x, iterate_line - 1) for pos_x in range(number_position[0] - 1, number_position[0] + len(content) + 1)] + 
                        [(number_position[0] - 1, iterate_line)] + [(number_position[0] + len(content), iterate_line)] + 
                        [(pos_x, iterate_line + 1) for pos_x in range(number_position[0] - 1, number_position[0] + len(content) + 1)]
                    )
                    
                    # Get the number to save
                    number = content
                    
                    # Save the found number
                    number_dict[(int(number), number_position)] = neighbors_possible_position
                
                # When the content is an operator
                else:
                    
                    # Handle gear
                    if content == "*":
                        
                        # Handle when same number are on the same line
                        if gear_position[1] == iterate_line:
                                            
                            # Get the start position of the number
                            gear_position = (gear_position[0] + len(gear) + line[gear_position[0] + len(gear):].find(content), iterate_line)
                        
                        # Handle the generic case
                        else:
                            
                            # Get the start position of the number
                            gear_position = (line.find(content), iterate_line)
                        
                        # Save operator
                        gear = content
                        
                        # Save the operator position
                        gear_position_set.add(gear_position)
                    
                    # Handle when same number are on the same line
                    if operator_position[1] == iterate_line:
                                        
                        # Get the start position of the number
                        operator_position = (operator_position[0] + len(operator) + line[operator_position[0] + len(operator):].find(content), iterate_line)
                    
                    # Handle the generic case
                    else:
                        
                        # Get the start position of the number
                        operator_position = (line.find(content), iterate_line)
                    
                    # Save operator
                    operator = content
                    
                    # Save the operator position
                    operator_position_set.add(operator_position)
                                     
        # Iterate through each found number
        number: int
        neighbors_possible_position: List[Tuple[int, int]]
        for (number, operator_position), neighbors_possible_position in number_dict.items():
            
            # Iterate through all neighbors possible position
            possible_position: Tuple[int, int]
            for possible_position in neighbors_possible_position:
                
                # Handle gear
                if possible_position in gear_position_set:
                    
                    gear_association_dict[possible_position] = gear_association_dict.get(possible_position, []) + [number]
                
                # Check if their is an operator at this position
                if possible_position in operator_position_set:
                    
                    # Add the number in the part 1 result
                    result_p1 += number
                    
                    # Early stop the process for this number
                    break
                        
        # Iterate through gear association
        gear: Tuple[int, int]
        association: List[int]
        for gear, association in gear_association_dict.items():
            
            # Check if it is a true gear
            if len(association) == 2:
                
                # Update the result of part 2
                result_p2 += association[0] * association[1] 
        
    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")