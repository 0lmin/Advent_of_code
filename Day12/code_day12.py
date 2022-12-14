# Set file to use as input
filename: str = 'input.txt'

# Create function computing neighbors list of a specific position in a height map
def get_neighbors(position: '(int, int)', height_map: dict) -> 'list((int, int))':
    """ 
    @Description:
        Return the list of all accessible neighbors of the current position in the height_map

    @Input:
        position:   (int, int) = Position at which finding the neighbors
        height_map: dict       = Height map in which finding the neighbors of the position

    @Output:
        neighbors_list: list((int, int)) = List of all accessible neighbors of position in 
                                           the height map
    """
    
    # Initialize list of neighbors
    neighbors_list: 'list((int, int))' = []
    
    # Set adjacency move map
    adj_move: 'list(int,int)' = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Iterate through all possible move
    for move in adj_move:
        
        # Compute new position
        new_position: '(int, int)' = (position[0] + move[0], position[1] + move[1])
        
        # Check if the position is legal
        if new_position in height_map:
            
            # Check that the position is accessible
            if ord(height_map[new_position]) - ord(height_map[position]) <= 1:
                
                # Add new position in the list of accessible neighbors
                neighbors_list.append(new_position)
                
    return neighbors_list

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = [line.rstrip() for line in f]
    
    # Initialize results sum
    result_p1: int = 0
    result_p2: int = 0
    
    # Part 1
    # Compute height map
    height_map: dict = {(iterate_line, iterate_char): char for iterate_line, line in enumerate(lines_list) 
                                                           for iterate_char, char in enumerate(line)}
    
    # Get starting and ending positions
    start: '(int, int)' = [key for key, value in height_map.items() if value == "S"][0]
    end:   '(int, int)' = [key for key, value in height_map.items() if value == "E"][0]
    
    # Replace at start and at end the correct height
    height_map[start] = 'a'
    height_map[end]   = 'z'
    
    # Initialize distance map
    dist_map: dict = {}
    
    # Use a Dijkstra algorithm
    # Initialize working queue for dijkstra
    working_queue: 'list((int, (int, int)))' = [(0, start)]
    
    # Iterate while working queue is not empty
    while len(working_queue) > 0:
        
        # Get position to study
        cost, position = working_queue.pop(0)
        
        # Skip value if position has already been seen
        if position in dist_map:
            continue
        # Else add it in the distance map
        else:
            dist_map[position] = cost
            
        # Complete path for all of its neighbors
        for neighbor in get_neighbors(position, height_map):
            
            # Add current neighbor in the working queue
            working_queue.append((cost + 1, neighbor))   
    
    # Compute shortest path the end
    result_p1 = dist_map[end]
    
    # Part 2
    # Compute height map (and replace starting position by its length)
    height_map: dict = {(iterate_line, iterate_char): char if char != 'S' else 'a' 
                                                           for iterate_line, line in enumerate(lines_list) 
                                                           for iterate_char, char in enumerate(line)}
    
    # Get starting list and ending positions
    start_list: 'list((int, int))' = [k for k, v in height_map.items() if v == "a"]
    end:   '(int, int)' = [k for k, v in height_map.items() if v == "E"][0]
    
    # Replace at end the correct height
    height_map[end]   = 'z'
    
    # Initialize distance map
    dist_map: dict = {}
    
    # Use a Dijkstra algorithm
    # Initialize working queue for dijkstra
    working_queue: 'list((int, (int, int)))' = [(0, start) for start in start_list]
    
    # Iterate while working queue is not empty
    while len(working_queue) > 0:
        
        # Get position to study
        cost, position = working_queue.pop(0)
        
        # Skip value if position has already been seen
        if position in dist_map:
            continue
        # Else add it in the distance map
        else:
            dist_map[position] = cost
            
        # Complete path for all of its neighbors
        for neighbor in get_neighbors(position, height_map):
            
            # Add current neighbor in the working queue
            working_queue.append((cost + 1, neighbor))      
    
    # Compute shortest path the end
    result_p2 = dist_map[end]
        
# Print results
print(f"{result_p1 = }")
print(f"{result_p2 = }")
