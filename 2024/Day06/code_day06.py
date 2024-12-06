# -*- coding: utf-8 -*-
"""
Created on Dec 06 2024

Last major update on v

@author: BERTIN Clément (0lmin)
 
Description:
Advent of Code (AoC) 2024 day 06
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List, Tuple, Set, Dict

################################################################################
############################## Functions #######################################
################################################################################

def goUp(current_position: Tuple[int, int],
         map_size: Tuple[int, int],
         obstacle_map: Set[Tuple[int, int]]) -> Tuple[Tuple[int, int], str]:
    """
    Apply the up movement to the guard.
    It return the next position of the guard and its state ("^", ">", "<", "v", "").
    If the guard goes out of the map, the output is [[-1,-1], '']
    """
    
    # Initialize the state
    state: str = "^"
    
    # Naively apply the up move
    naive_position: Tuple[int, int] = (current_position[0], current_position[1] - 1)
    
    # Check if an obstacle is at the naive new position and update the state
    if naive_position in obstacle_map:
        
        # Update the position
        naive_position, state = goRight(current_position,
                                        map_size,
                                        obstacle_map)
    
    # Check if the new position is out of the map
    if naive_position[0] > map_size[0] or \
       naive_position[0] < 0 or \
       naive_position[1] > map_size[1] or \
       naive_position[1] < 0:
           
        # Update the position
        naive_position = (-1, -1)
        state = ""
        
    return (naive_position, state)

def goRight(current_position: Tuple[int, int],
            map_size: Tuple[int, int],
            obstacle_map: Set[Tuple[int, int]]) -> Tuple[Tuple[int, int], str]:
    """
    Apply the right movement to the guard.
    It return the next position of the guard and its state ("^", ">", "<", "v", "").
    If the guard goes out of the map, the output is [[-1,-1], '']
    """
    # Initialize the state
    state: str = ">"
    
    # Naively apply the up move
    naive_position: Tuple[int, int] = (current_position[0] + 1, current_position[1])
    
    # Check if an obstacle is at the naive new position and update the state
    if naive_position in obstacle_map:
        
        # Update the position
        naive_position, state = goDown(current_position,
                                        map_size,
                                        obstacle_map)
    
    # Check if the new position is out of the map
    if naive_position[0] > map_size[0] or \
       naive_position[0] < 0 or \
       naive_position[1] > map_size[1] or \
       naive_position[1] < 0:
           
        # Update the position
        naive_position = (-1, -1)
        state = ""
        
    return (naive_position, state)

def goDown(current_position: Tuple[int, int],
           map_size: Tuple[int, int],
           obstacle_map: Set[Tuple[int, int]]) -> Tuple[Tuple[int, int], str]:
    """
    Apply the down movement to the guard.
    It return the next position of the guard and its state ("^", ">", "<", "v", "").
    If the guard goes out of the map, the output is [[-1,-1], '']
    """
    # Initialize the state
    state: str = "v"
    
    # Naively apply the up move
    naive_position: Tuple[int, int] = (current_position[0], current_position[1] + 1)
    
    # Check if an obstacle is at the naive new position and update the state
    if naive_position in obstacle_map:
        
        # Update the position
        naive_position, state = goLeft(current_position,
                                        map_size,
                                        obstacle_map)
    
    # Check if the new position is out of the map
    if naive_position[0] > map_size[0] or \
       naive_position[0] < 0 or \
       naive_position[1] > map_size[1] or \
       naive_position[1] < 0:
           
        # Update the position
        naive_position = (-1, -1)
        state = ""
        
    return (naive_position, state)

def goLeft(current_position: Tuple[int, int],
           map_size: Tuple[int, int],
           obstacle_map: Set[Tuple[int, int]]) -> Tuple[Tuple[int, int], str]:
    """
    Apply the left movement to the guard.
    It return the next position of the guard and its state ("^", ">", "<", "v", "").
    If the guard goes out of the map, the output is [[-1,-1], '']
    """
    # Initialize the state
    state: str = "<"
    
    # Naively apply the up move
    naive_position: Tuple[int, int] = (current_position[0] - 1, current_position[1])
    
    # Check if an obstacle is at the naive new position and update the state
    if naive_position in obstacle_map:
        
        # Update the position
        naive_position, state = goUp(current_position,
                                        map_size,
                                        obstacle_map)
    
    # Check if the new position is out of the map
    if naive_position[0] > map_size[0] or \
       naive_position[0] < 0 or \
       naive_position[1] > map_size[1] or \
       naive_position[1] < 0:
           
        # Update the position
        naive_position = (-1, -1)
        state = ""
        
    return (naive_position, state)
    
################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":
    
    # Set file to use as input
    filename: str = "2024/Day06/input.txt"

    # Get file content
    f: StringIO
    with open(filename) as f:
        
        # Read all lines
        lines_list: List[str] = list(map(lambda line: line.replace("\n", ""), f.readlines()))
        
        # Get the map dimension
        map_size: Tuple[int, int] = [len(lines_list[0]) - 1, len(lines_list) - 1]
        
        # Initialize the list of obstacle
        obstacle_map: Set[Tuple[int, int]] = set()
        
        # Iterate through the input lines
        iterate_line: int
        line: str
        for iterate_line, line in enumerate(lines_list):
            
            iterate_char: int
            char: str
            for iterate_char, char in enumerate(line):
                
                # Check if it is the initial guard's position
                if char == "^":
                    
                    # Store the initial position of the guard
                    guard_position: Tuple[int, int] = (iterate_char, iterate_line)
                
                # Check if there is an obstacle
                if char == "#":
                    
                    # Store a new obstacle
                    obstacle_map.add((iterate_char, iterate_line))
                    
        # Save the initial position
        guard_init_position: Tuple[int, int] = guard_position
        
        # Part 1        
        # Initialize the guard's state
        guard_state: str = "^"
        
        # Initialize the set of the guard's position and state
        guard_position_state_dict: Dict[Tuple[int, int], List[str]] = dict()
        
        # Iterate until the guard goes out of the map or restart its path
        while guard_state != "" and \
            (not(guard_position in guard_position_state_dict.keys()) or not(guard_state in guard_position_state_dict[guard_position])):
            
            # Add the current position state of the guard
            if guard_position in guard_position_state_dict.keys():
                guard_position_state_dict[guard_position].append(guard_state)
            else:
                guard_position_state_dict[guard_position] = [guard_state]
            
            # Apply a specific move depending on the guard's state
            if guard_state == "^":
                
                # Go up
                guard_position, guard_state = goUp(guard_position,
                                                   map_size,
                                                   obstacle_map)
                
            # Apply a specific move depending on the guard's state
            elif guard_state == ">":
                
                # Go right
                guard_position, guard_state = goRight(guard_position,
                                                      map_size,
                                                      obstacle_map)
                
            # Apply a specific move depending on the guard's state
            elif guard_state == "v":
                
                # Go down
                guard_position, guard_state = goDown(guard_position,
                                                     map_size,
                                                     obstacle_map)
                
            # Apply a specific move depending on the guard's state
            elif guard_state == "<":
                
                # Go left
                guard_position, guard_state = goLeft(guard_position,
                                                     map_size,
                                                     obstacle_map)
                
        # Compute the number of position of the guard
        result_p1: int = len(guard_position_state_dict.keys())
        
        # Print results
        print(f"{result_p1 = }")
        
        # Part 2
        # Initialize the result of part 2
        result_p2: int = 0
        
        # Iterate through all possible location of a new obstacle
        x: int
        for x in range(map_size[0] + 1):
            y: int
            for y in range(map_size[1] + 1):
                
                # Create a deep copy of the obstacle map
                obstacle_map_test: Set[Tuple[int, int]] = obstacle_map.copy()
                
                # Check if an obstacle can be placed here
                if (x, y) in obstacle_map or (x, y) == guard_init_position:
                    
                    # Go to next iteration
                    continue
                
                # Add an obstacle in the current position
                obstacle_map_test.add((x, y))

                # Initialize the guard position
                guard_position = guard_init_position
        
                # Initialize the guard's state
                guard_state: str = "^"
                
                # Initialize the set of the guard's position and state
                guard_position_state_dict: Dict[Tuple[int, int], List[str]] = dict()
                
                # Iterate until the guard goes out of the map or restart its path
                while guard_state != "" and \
                    (not(guard_position in guard_position_state_dict.keys()) or not(guard_state in guard_position_state_dict[guard_position])):
                    
                    # Add the current position state of the guard
                    if guard_position in guard_position_state_dict.keys():
                        guard_position_state_dict[guard_position].append(guard_state)
                    else:
                        guard_position_state_dict[guard_position] = [guard_state]
                    
                    # Apply a specific move depending on the guard's state
                    if guard_state == "^":
                        
                        # Go up
                        guard_position, guard_state = goUp(guard_position,
                                                           map_size,
                                                           obstacle_map_test)
                        
                    # Apply a specific move depending on the guard's state
                    elif guard_state == ">":
                        
                        # Go right
                        guard_position, guard_state = goRight(guard_position,
                                                            map_size,
                                                            obstacle_map_test)
                        
                    # Apply a specific move depending on the guard's state
                    elif guard_state == "v":
                        
                        # Go down
                        guard_position, guard_state = goDown(guard_position,
                                                            map_size,
                                                            obstacle_map_test)
                        
                    # Apply a specific move depending on the guard's state
                    elif guard_state == "<":
                        
                        # Go left
                        guard_position, guard_state = goLeft(guard_position,
                                                             map_size,
                                                             obstacle_map_test)
                
                # Check if a loop has been found
                if guard_position in guard_position_state_dict.keys() and guard_state in guard_position_state_dict[guard_position]:
                    
                    # Update the result of part 2
                    result_p2 += 1
                
        # Print results
        print(f"{result_p2 = }")