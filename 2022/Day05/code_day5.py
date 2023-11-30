# -*- coding: utf-8 -*-
"""
Created on Dec 05 2022

Last major update on Nov 30 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 5's challenge of the Advent of Code (AoC)
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List

# Import deepcopy
from copy import deepcopy

################################################################################
############################### Function #######################################
################################################################################

def getStartingPosition(position_list: List[str]) -> List[str]:
        """
        @Description:
           Compute a list of stack corresponding to the starting position 

        @Input:
            - position_list:
                List of all the positions at the start

        @Output:
            - starting_position:
                Starting position represented as a list of list (stack) for 
                each column
        """
        
        # Create empty position
        nb_stack: int = len(position_list[-1].split('  '))
        starting_position: List[str] = [[] for _ in range(nb_stack)]
        
        # Remove axis
        position_list: List[str] = position_list[:-1]
        
        # Iterate through all lines of the reversed list of lines
        line: str
        for line in position_list[::-1]:

            # Iterate through current line 4 by 4
            stack_index: int
            content_index: str
            for stack_index, content_index in enumerate(range(0, len(line), 4)):
                
                # Get current content
                content: str = line[content_index:(content_index + 4)]
                
                # Add in stack if needed
                if content != '    ':
                    starting_position[stack_index].append(content[1])
                    
        # Return list of stack at starting position
        return starting_position
    
################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":

    # Set file to use as input
    filename: str = '2022/Day05/input.txt'

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = [line.rstrip() for line in f]
        
        # Get separation between position and move
        separation_index: int = lines_list[:-1].index('')
        
        # Separate move and starting position
        position_p1: List[str] = getStartingPosition(lines_list[:separation_index])
        position_p2: List[str] = deepcopy(position_p1)
        
        # Remove starting position to only get moves
        moves_list: List[str] = lines_list[separation_index+1:]
        
        # Iterate through moves
        move: str
        for move in moves_list:
            
            # Get destination stack
            destination_stack_index: int = int(move.split(' to ')[-1]) - 1
            move = move.split(' to ')[0]

            # Get origin stack
            origin_stack_index: int = int(move.split(' from ')[-1]) - 1
            move = move.split(' from ')[0]
            
            # Get number of move
            nb_move: int = int(move.split('move ')[-1])
            
            # Apply moves for this line for part 1
            for _ in range(nb_move):
                position_p1[destination_stack_index].append(position_p1[origin_stack_index].pop())
                
            # Apply moves for this line for part 2
            position_p2[destination_stack_index] += position_p2[origin_stack_index][-nb_move:]
            position_p2[origin_stack_index] = position_p2[origin_stack_index][:-nb_move]
                
        # Compute result_p1 after all moves
        result_p1: str = ''.join([stack[-1] for stack in position_p1])
        result_p2: str = ''.join([stack[-1] for stack in position_p2])

    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")