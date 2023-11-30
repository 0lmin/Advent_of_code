# -*- coding: utf-8 -*-
"""
Created on Dec 09 2022

Last major update on Nov 30 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 9's challenge of the Advent of Code (AoC)
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List, Tuple, Set, Dict

################################################################################
############################### Function #######################################
################################################################################

def moveOnce(head: Tuple[int, int], 
             tail: Tuple[int, int]) -> Tuple[int, int]:
    """
    @Description:
    -------------
        Process to a one step move
    
    @Input:
    -------
        - head:
            Position of the head
        - tail:
            Position of the tail
    
    @Output:
    --------
        - tail:
            Position of the moved tail
    """
    
    # Compute gap between head and tail
    path: Tuple[int, int] = [head[0] - tail[0], head[1] - tail[1]]
    
    # Detect if tail need to move
    limited_path: Tuple[int, int] = [max(min(head[0] - tail[0], 1), -1), 
                                     max(min(head[1] - tail[1], 1), -1)]
    
    # Check if the vector head-tail is not limited
    if path != limited_path:
        
        # Add limited path to fill the delay
        return [tail[0] + limited_path[0], tail[1] + limited_path[1]] 
    return tail

################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":

    # Set file to use as input
    filename: str = '2022/Day09/input.txt'

    # Create dictionary representing each possible move
    move_dir: Dict[str, Tuple[int, int]] = {
        "R": [1, 0],
        "L": [-1, 0],
        "U": [0, 1],
        "D": [0, -1]
    }

    # Define number of knot for part 2
    nb_knot: int = 10

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = [line.rstrip() for line in f]
        
        # Initialize results sum
        result_p1: int = 0
        result_p2: int = 0
        
        # Part 1
        # Initialize head and tail
        head: Tuple[int, int] = [0, 0]
        tail: Tuple[int, int] = [0, 0]
        
        # Initialize seen positions
        seen_positions: Set[Tuple[int, int]] = {(0,0)}
        
        # Iterate through each move
        line: str
        for line in lines_list:
            
            # Extract data from line
            splitted_line: Tuple[str, str] = line.split(' ')
            move: Tuple[int, int] = move_dir[splitted_line[0]]
            nb_step: int = int(splitted_line[1])
            
            # Iterate through each step
            for _ in range(nb_step):
                
                # Update position of the head
                head = [head[0] + move[0], head[1] + move[1]]
                
                # Update tail
                tail = moveOnce(head, tail)
                
                # Add position in the seen positions
                seen_positions.add(tuple(tail))
                
        # Compute result for part 1
        result_p1 = len(seen_positions)
        
        # Part 2
        # Initialize all knots
        knots: List[Tuple[int, int]] = [[0, 0] for _ in range(nb_knot)]
        
        # Initialize seen positions
        seen_positions: Set[Tuple[int, int]] = {(0,0)}
        
        # Iterate through each move
        line: str
        for line in lines_list:
            
            # Extract data from line
            splitted_line: Tuple[str, str] = line.split(' ')
            move: Tuple[int, int] = move_dir[splitted_line[0]]
            nb_step: int = int(splitted_line[1])
            
            # Iterate through each step
            for _ in range(nb_step):
                
                # Update position of the head
                knots[0] = [knots[0][0] + move[0], knots[0][1] + move[1]]
                
                # Iterate through each knots
                iterate_knots: int
                for iterate_knots in range(1, nb_knot):
                    
                    # Make current knot move
                    knots[iterate_knots] = moveOnce(knots[iterate_knots - 1], knots[iterate_knots])
                    
                # Add position of the last knots in the seen positions
                seen_positions.add(tuple(knots[-1]))
                
        # Compute result for part 2
        result_p2 = len(seen_positions)
        
    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")