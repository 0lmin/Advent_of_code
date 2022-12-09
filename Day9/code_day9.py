# Import deepcopy
from copy import deepcopy

# Set file to use as input
filename: str = 'input.txt'

# Create dictionary representing each possible move
move_dir = {"R": [1, 0],
            "L": [-1, 0],
            "U": [0, 1],
            "D": [0, -1]}

# Define number of knot for part 2
nb_knot: int = 10

def move_once(head: '[int, int]', tail: '[int, int]') -> '[int, int]':
    
    # Compute gap to 
    path: '[int, int]' = [head[0] - tail[0], head[1] - tail[1]]
    
    # Detect if tail need to move
    limited_path = [max(min(head[0] - tail[0], 1), -1), max(min(head[1] - tail[1], 1), -1)]
    if path != limited_path:
        
        # Add limited path to fill the delay
        return [tail[0] + limited_path[0], tail[1] + limited_path[1]] 
    return tail

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = [line.rstrip() for line in f]
    
    # Initialize results sum
    result_p1: int = 0
    result_p2: int = 0
    
    # Part 1
    # Initialize head and tail
    head: '[int, int]' = [0, 0]
    tail: '[int, int]' = [0, 0]
    
    # Initialize seen positions
    seen_positions: set = {(0,0)}
    
    # Iterate through each move
    for line in lines_list:
        
        # Extract data from line
        splitted_line: '[str, str]' = line.split(' ')
        move: tuple = move_dir[splitted_line[0]]
        nb_step: int = int(splitted_line[1])
        
        # Iterate through each step
        for _ in range(nb_step):
            
            # Update position of the head
            head = [head[0] + move[0], head[1] + move[1]]
            
            # Update tail
            tail = move_once(head, tail)
            
            # Add position in the seen positions
            seen_positions.add(tuple(tail))
            
    # Compute result for part 1
    result_p1 = len(seen_positions)
    
    # Part 2
    # Initialize all knots
    knots: '[[int, int] * nb_knot]' = [[0, 0] for _ in range(nb_knot)]
    
    # Initialize seen positions
    seen_positions: set = {(0,0)}
    
    # Iterate through each move
    for line in lines_list:
        
        # Extract data from line
        splitted_line: '[str, str]' = line.split(' ')
        move: tuple = move_dir[splitted_line[0]]
        nb_step: int = int(splitted_line[1])
        
        # Iterate through each step
        for _ in range(nb_step):
            
            # Update position of the head
            knots[0] = [knots[0][0] + move[0], knots[0][1] + move[1]]
            
            # Iterate through each knots
            for iterate_knots in range(1, nb_knot):
                
                # Make current knot move
                knots[iterate_knots] = move_once(knots[iterate_knots - 1], knots[iterate_knots])
                
            # Add position of the last knots in the seen positions
            seen_positions.add(tuple(knots[-1]))
            
    # Compute result for part 2
    result_p2 = len(seen_positions)
     
# Print results
print(f"{result_p1 = }")
print(f"{result_p2 = }")