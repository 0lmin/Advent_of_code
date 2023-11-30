# -*- coding: utf-8 -*-
"""
Created on Dec 08 2022

Last major update on Nov 30 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 8's challenge of the Advent of Code (AoC)
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List, Tuple, Set

# Import deepcopy
from copy import deepcopy

################################################################################
################################ Function ######################################
################################################################################

def compute_tree_maps(lines_list: List[str]) -> Tuple[List[List[int]], 
                                                      List[List[int]], 
                                                      List[List[int]], 
                                                      List[List[int]], 
                                                      List[List[int]]]:
    """
    @Description:
        Compute the tree map according to the string description

    @Input:
        - lines_list: 
            Description of the tree map

    @Output:
        - full_tree_map: 
            Tree map extracted from the description
        - tree_map_north: 
            Tree map seen from the north
        - tree_map_south: 
            Tree map seen from the south
        - tree_map_west:  
            Tree map seen from the west
        - tree_map_east:  
            Tree map seen from the east
    """
    
    # Initialize the tree map
    full_tree_map: List[List[int]] = []
    
    # Iterate through all lines
    line: str
    for line in lines_list:
        
        # Add a new line of tree in the map (and add 1 to scale the trees)
        full_tree_map.append(list(map(int, line)))

    # # Copy full_tree_map for each view
    tree_map_north: List[List[int]] = deepcopy(full_tree_map)
    tree_map_south: List[List[int]] = deepcopy(full_tree_map)
    tree_map_west: List[List[int]] = deepcopy(full_tree_map)
    tree_map_east: List[List[int]] = deepcopy(full_tree_map)
    
    # Compute size of the map
    map_size: int = len(full_tree_map)
    
    # Compute tree map seen from the west
    tree_line_index: int
    tree_line: List[int]
    for tree_line_index, tree_line in enumerate(full_tree_map):
        
        # Initialize the maximum tree size encountered for each line
        max_tree: int = 0
        
        # Iterate through each item of the tree line
        tree_row_index: int
        tree: int
        for tree_row_index, tree in enumerate(tree_line[:-1]):
            
            # Update max tree size encountered if necessary
            if tree > max_tree:
                max_tree = tree
            
            # Update diff map for the current value
            tree_map_west[tree_line_index][tree_row_index + 1] -= max_tree
                 
    # Compute tree map seen from the east
    tree_line_index: int
    tree_line: List[int]
    for tree_line_index, tree_line in enumerate(full_tree_map):
        
        # Initialize the maximum tree size encountered for each line
        max_tree: int = 0
        
        # Iterate through each item of the tree line
        tree_row_index: int
        tree: int
        for tree_row_index, tree in enumerate(tree_line[::-1][:-1]):
            
            # Update max tree size encountered if necessary
            if tree > max_tree:
                max_tree = tree
            
            # Update diff map for the current value
            tree_map_east[tree_line_index][map_size - (tree_row_index + 2)] -= max_tree
            
    # Compute tree map seen from the north
    tree_row_index: int
    tree_row: List[int]
    for tree_row_index, tree_row in enumerate(list(map(list, zip(*full_tree_map)))): # Transpose map
        
        # Initialize the maximum tree size encountered for each row
        max_tree: int = 0
        
        # Iterate through each item of the tree row
        tree_line_index: int
        tree: int
        for tree_line_index, tree in enumerate(tree_row[:-1]):
            
            # Update max tree size encountered if necessary
            if tree > max_tree:
                max_tree = tree
            
            # Update diff map for the current value
            tree_map_north[tree_line_index + 1][tree_row_index] -= max_tree
                 
    # Compute tree map seen from the south
    tree_row_index: int
    tree_row: List[int]
    for tree_row_index, tree_row in enumerate(list(map(list, zip(*full_tree_map)))): # Transpose map
        
        # Initialize the maximum tree size encountered for each row
        max_tree: int = 0
        
        # Iterate through each item of the tree row
        tree_line_index: int
        tree: int
        for tree_line_index, tree in enumerate(tree_row[::-1][:-1]):
            
            # Update max tree size encountered if necessary
            if tree > max_tree:
                max_tree = tree
            
            # Update diff map for the current value
            tree_map_south[map_size - (tree_line_index + 2)][tree_row_index] -= max_tree
    
    # The tree view is the same from each point of 
    return full_tree_map, tree_map_north, tree_map_south, tree_map_west, tree_map_east                            

def update_seen_trees(tree_map: List[List[int]],
                      seen_trees: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    """
    @Description:
        Update the dict of seen trees

    @Input:
        - tree_map:
            Map of the trees seen from a certain perspective
        - seen_trees:
            Set of all seen trees (position in the map)

    @Output:
        - seen_trees: 
            Updated set of seen trees
    """
    
    # Iterate through all line in of the matrix
    line_index: int
    tree_line: List[int]
    for line_index, tree_line in enumerate(tree_map[1:-1]):
        
        # Iterate through all trees
        row_index: int
        tree: int
        for row_index, tree in enumerate(tree_line[1:-1]):
            
            # If the tree can be seen, add it in the set
            if tree > 0:
                seen_trees.add((line_index + 1, row_index + 1))
                
    return seen_trees

################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":

    # Set file to use as input
    filename: str = '2022/Day08/input.txt'

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = [line.rstrip() for line in f]
        
        # Initialize results sum
        result_p1: int = 0
        result_p2: int = 0
        
        # Compute result of the part 1    
        # Get the correctly formatted tree map
        full_tree_map: List[List[int]]
        tree_map_north: List[List[int]]
        tree_map_south: List[List[int]]
        tree_map_west: List[List[int]]
        tree_map_east: List[List[int]]
        full_tree_map, tree_map_north, tree_map_south, tree_map_west, tree_map_east = compute_tree_maps(lines_list)
        
        # Initialize dict of seen trees
        seen_trees: Set[Tuple[int, int]] = set()
        
        # Update seen trees from the north
        seen_trees = update_seen_trees(tree_map_north, seen_trees)   
        
        # Update seen trees from the south
        seen_trees = update_seen_trees(tree_map_south, seen_trees)

        # Update seen trees from the west
        seen_trees = update_seen_trees(tree_map_west, seen_trees)
        
        # Update seen trees from the east
        seen_trees = update_seen_trees(tree_map_east, seen_trees)
    
        # Compute result for part1
        result_p1: int = len(seen_trees) + (len(tree_map_north) ** 2 - (len(tree_map_north) - 2) ** 2)
        
        # Compute result of the part 2
        # Initialize result for each direction
        north_view: List[int] = []
        south_view: List[int] = []
        west_view: List[int] = []
        east_view: List[int] = []
        
        # Iterate through map
        tree_line_index: int
        tree_line: List[int]
        for tree_line_index, tree_line in enumerate(full_tree_map):
            
            tree_row_index: int
            tree: int
            for tree_row_index, tree in enumerate(tree_line):
                
                # Initialize view for the current tree
                north_view.append(0)
                west_view.append(0)
                south_view.append(0)
                east_view.append(0)
                
                # Compute seen tree to the north
                j: int
                for j in range(tree_row_index - 1, -1, -1):
                    
                    # Update counter
                    north_view[-1] += 1
                    
                    # Detect if we need to stop in this direction
                    if full_tree_map[tree_line_index][j] >= tree:
                        break
                    
                # Compute seen tree to the west
                i: int
                for i in range(tree_line_index - 1, -1, -1):
                    
                    # Update counter
                    west_view[-1] += 1
                    
                    # Detect if we need to stop in this direction
                    if full_tree_map[i][tree_row_index] >= tree:
                        break
        
                # Compute seen tree to the south
                j: int
                for j in range(tree_row_index + 1, len(tree_line)):
                    
                    # Update counter
                    south_view[-1] += 1
                    
                    # Detect if we need to stop in this direction
                    if full_tree_map[tree_line_index][j] >= tree:
                        break
        
                # Compute seen tree to the east
                i: int
                for i in range(tree_line_index + 1, len(full_tree_map)):
                    
                    # Update counter
                    east_view[-1] += 1
                    
                    # Detect if we need to stop in this direction
                    if full_tree_map[i][tree_row_index] >= tree:
                        break
                    
        # Compute total score for all the trees
        score: List[int] = [north_view[i] * south_view[i] * west_view[i] * east_view[i] for i in range(len(north_view))]
        
        # Compute result for part 2
        result_p2 = max(score)
                    
    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")