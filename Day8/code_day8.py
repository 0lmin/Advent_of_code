# Import deepcopy
from copy import deepcopy

# Set file to use as input
filename: str = 'input.txt'

def compute_tree_maps(lines_list: 'list(str)') -> '[list(list(int)), list(list(int)), list(list(int)), list(list(int)), list(list(int))]':
    """
    @Description:
        Return the tree map according to the string description

    @Input:
        lines_list: list(str) = Description of the tree map

    @Output:
        full_tree_map : list(list(int)) = Tree map extracted from the description
        tree_map_north: list(list(int)) = Tree map seen from the north
        tree_map_south: list(list(int)) = Tree map seen from the south
        tree_map_west:  list(list(int)) = Tree map seen from the west
        tree_map_east:  list(list(int)) = Tree map seen from the east
    """
    
    # Initialize the tree map
    full_tree_map: 'list(list(int))' = []
    
    # Iterate through all lines
    for line in lines_list:
        
        # Add a new line of tree in the map (and add 1 to scale the trees)
        full_tree_map.append(list(map(int, line)))

        
    # # Copy full_tree_map for each view
    tree_map_north: 'list(list(int))' = deepcopy(full_tree_map)
    tree_map_south: 'list(list(int))' = deepcopy(full_tree_map)
    tree_map_west: 'list(list(int))' = deepcopy(full_tree_map)
    tree_map_east: 'list(list(int))' = deepcopy(full_tree_map)
    
    # Compute size of the map
    map_size: int = len(full_tree_map)
    
    # Compute tree map seen from the west
    for tree_line_index, tree_line in enumerate(full_tree_map):
        
        # Initialize the maximum tree size encountered for each line
        max_tree = 0
        
        for tree_row_index, tree in enumerate(tree_line[:-1]):
            
            # Update max tree size encountered if necessary
            if tree > max_tree:
                max_tree = tree
            
            # Update diff map for the current value
            tree_map_west[tree_line_index][tree_row_index + 1] -= max_tree
                 
    # Compute tree map seen from the east
    for tree_line_index, tree_line in enumerate(full_tree_map):
        
        # Initialize the maximum tree size encountered for each line
        max_tree = 0
        
        for tree_row_index, tree in enumerate(tree_line[::-1][:-1]):
            
            # Update max tree size encountered if necessary
            if tree > max_tree:
                max_tree = tree
            
            # Update diff map for the current value
            tree_map_east[tree_line_index][map_size - (tree_row_index + 2)] -= max_tree
            
    # Compute tree map seen from the north
    for tree_row_index, tree_row in enumerate(list(map(list, zip(*full_tree_map)))): # Transpose map
        
        # Initialize the maximum tree size encountered for each row
        max_tree = 0
        
        for tree_line_index, tree in enumerate(tree_row[:-1]):
            
            # Update max tree size encountered if necessary
            if tree > max_tree:
                max_tree = tree
            
            # Update diff map for the current value
            tree_map_north[tree_line_index + 1][tree_row_index] -= max_tree
                 
    # Compute tree map seen from the south
    for tree_row_index, tree_row in enumerate(list(map(list, zip(*full_tree_map)))): # Transpose map
        
        # Initialize the maximum tree size encountered for each row
        max_tree = 0
        
        for tree_line_index, tree in enumerate(tree_row[::-1][:-1]):
            
            # Update max tree size encountered if necessary
            if tree > max_tree:
                max_tree = tree
            
            # Update diff map for the current value
            tree_map_south[map_size - (tree_line_index + 2)][tree_row_index] -= max_tree
    
    # The tree view is the same from each point of 
    return full_tree_map, tree_map_north, tree_map_south, tree_map_west, tree_map_east                            

def update_seen_trees(tree_map: 'list(list(int))',
                      seen_trees: set) -> 'set':
    """
    @Description:
        Return the updated dict of seen trees

    @Input:
        tree_map:   list(list(int)) = Map of the trees seen from a certain perspective
        seen_trees: set             = Set of all seen trees (position in the map)

    @Output:
        seen_trees: set = Updated set of seen trees
    """
    
    # Iterate through all line in of the matrix
    for line_index, tree_line in enumerate(tree_map[1:-1]):
        
        # Iterate through all trees
        for row_index, tree in enumerate(tree_line[1:-1]):
            
            # If the tree can be seen, add it in the set
            if tree > 0:
                seen_trees.add((line_index + 1, row_index + 1))
                
    return seen_trees

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = [line.rstrip() for line in f]
    
    # Initialize results sum
    result_p1: int = 0
    result_p2: int = 0
    
    # Compute result of the part 1    
    # Get the correctly formatted tree map
    full_tree_map, tree_map_north, tree_map_south, tree_map_west, tree_map_east = compute_tree_maps(lines_list)
    
    # Initialize dict of seen trees
    seen_trees: set = set()
    
    # Update seen trees from the north
    seen_trees = update_seen_trees(tree_map_north, seen_trees)   
    
    # Update seen trees from the south
    seen_trees = update_seen_trees(tree_map_south, seen_trees)

    # Update seen trees from the west
    seen_trees = update_seen_trees(tree_map_west, seen_trees)
    
    # Update seen trees from the east
    seen_trees = update_seen_trees(tree_map_east, seen_trees)
   
    # Compute result for part1
    result_p1 = len(seen_trees) + (len(tree_map_north) ** 2 - (len(tree_map_north) - 2) ** 2)
    
    # Compute result of the part 2
    # Initialize result for each direction
    north_view: 'list(int)' = []
    south_view: 'list(int)' = []
    west_view: 'list(int)' = []
    east_view: 'list(int)' = []
    
    # Iterate through map
    for tree_line_index, tree_line in enumerate(full_tree_map):
        for tree_row_index, tree in enumerate(tree_line):
            
            # Initialize view for the current tree
            north_view.append(0)
            west_view.append(0)
            south_view.append(0)
            east_view.append(0)
            
            # Compute seen tree to the north
            for j in range(tree_row_index - 1, -1, -1):
                
                # Update counter
                north_view[-1] += 1
                
                # Detect if we need to stop in this direction
                if full_tree_map[tree_line_index][j] >= tree:
                    break
                
            # Compute seen tree to the west
            for i in range(tree_line_index - 1, -1, -1):
                
                # Update counter
                west_view[-1] += 1
                
                # Detect if we need to stop in this direction
                if full_tree_map[i][tree_row_index] >= tree:
                    break
    
            # Compute seen tree to the south
            for j in range(tree_row_index + 1, len(tree_line)):
                
                # Update counter
                south_view[-1] += 1
                
                # Detect if we need to stop in this direction
                if full_tree_map[tree_line_index][j] >= tree:
                    break
    
            # Compute seen tree to the east
            for i in range(tree_line_index + 1, len(full_tree_map)):
                
                # Update counter
                east_view[-1] += 1
                
                # Detect if we need to stop in this direction
                if full_tree_map[i][tree_row_index] >= tree:
                    break
                
    # Compute total score for all the trees
    score = [north_view[i] * south_view[i] * west_view[i] * east_view[i] for i in range(len(north_view))]
    
    # Compute result for part 2
    result_p2 = max(score)
                
# Print results
print(f"{result_p1 = }")
print(f"{result_p2 = }")