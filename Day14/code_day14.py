# Set file to use as input
filename: str = 'input.txt'

# Set starting position of the sand
sand_start: '(int, int)' = (500, 0)

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = [line.rstrip() for line in f]
    
    # Initialize results sum
    result_p1: int = 0
    result_p2: int = 0
    
    # Set the set of all the rock position
    rock_positions: set = set()
    
    # Iterate through each rock path
    for line in lines_list:
        
        # Compute all the key position of each rock path
        rock_path_position_list: 'list((int, int))' = list(map(lambda position_str: tuple(map(int, position_str.split(','))),
                                                             line.split(' -> ')))
        
        # Add rocks to the set of rock
        for position_index in range(len(rock_path_position_list) - 1):
            
            # Compute start and end of the straight line
            start_position: '(int, int)' = rock_path_position_list[position_index]
            end_position:   '(int, int)' = rock_path_position_list[position_index + 1]
            
            # Dissociate vertical and horizontal straight lines
            # Handle vertical straight line case
            if start_position[0] == end_position[0]:
                
                # Iteratively add each rock of the straight line in the set of rocks
                for rock_y in range(min(start_position[1], end_position[1]), max(start_position[1], end_position[1]) + 1):
                    
                    # Add current rock position to the set
                    rock_positions.add((start_position[0], rock_y))
                
            # Handle horizontal straight line case
            else:
                
                # Iteratively add each rock of the straight line in the set of rocks
                for rock_x in range(min(start_position[0], end_position[0]), max(start_position[0], end_position[0]) + 1):
                    
                    # Add current rock position to the set
                    rock_positions.add((rock_x, start_position[1]))
                    
        # Get the lowest rock position in the set
        lowest_rock_position: int = max(list(rock_positions), key = lambda position: position[1])
        
    # Save the rock positions
    saved_rock_position: set = rock_positions.copy()
        
    # Set the position of sand block
    sand_position: '(int, int)' = sand_start
    
    # Initialize the number of sand block that have fall
    fall_sand_block_counter: int = 1
    
    # Compute part 1    
    # Compute sand move while its needed
    while sand_position[1] < lowest_rock_position[1]:
        
        # Detect if the sand block can't move down
        if (sand_position[0], sand_position[1] + 1) in rock_positions:
            
            # Detect if the sand block can't move down to the left
            if (sand_position[0] - 1, sand_position[1] + 1) in rock_positions:
                
                # Detect if the sand block can't move down to the right
                if (sand_position[0] + 1, sand_position[1] + 1) in rock_positions:
                    
                    # Add fall sand block position as a new rock
                    rock_positions.add(sand_position)
                    
                    # Make a new sand block fall
                    sand_position = sand_start
                    
                    # Update the number of fall sand block
                    fall_sand_block_counter += 1
                
                # Make the sand block move to the down right
                else:
                    
                    # Update sand block position
                    sand_position = (sand_position[0] + 1, sand_position[1] + 1)
            
            # Make the sand block move to the down left
            else:

                # Update sand block position
                sand_position = (sand_position[0] - 1, sand_position[1] + 1)
                
        # Make the sand block move to the down
        else:

            # Update sand block position
            sand_position = (sand_position[0], sand_position[1] + 1)
            
    # Compute result for part 1
    result_p1 = fall_sand_block_counter - 1
        
        
    # Compute part 2
    # Reset the rock positions set
    rock_positions = saved_rock_position.copy()
    
    # Initialize the number of sand block that have fall
    fall_sand_block_counter: int = 1
    
    # Compute floor y position
    floor_y: int = lowest_rock_position[1] + 2
    
    # Compute sand move while possible
    while True:
        
        # Detect if the sand block can't move down
        if ((sand_position[0], sand_position[1] + 1) in rock_positions or
            (sand_position[1] + 1 == floor_y)):
            
            # Detect if the sand block can't move down to the left
            if ((sand_position[0] - 1, sand_position[1] + 1) in rock_positions or
                (sand_position[1] + 1 == floor_y)):
                
                # Detect if the sand block can't move down to the right
                if ((sand_position[0] + 1, sand_position[1] + 1) in rock_positions or
                    (sand_position[1] + 1 == floor_y)):
                    
                    # Detect end of fall
                    if sand_position == sand_start:
                        break
                    
                    # Else continue to simulate the sand fall
                    else:
                    
                        # Add fall sand block position as a new rock
                        rock_positions.add(sand_position)
                        
                        # Make a new sand block fall
                        sand_position = sand_start
                        
                        # Update the number of fall sand block
                        fall_sand_block_counter += 1
                
                # Make the sand block move to the down right
                else:
                    
                    # Update sand block position
                    sand_position = (sand_position[0] + 1, sand_position[1] + 1)
            
            # Make the sand block move to the down left
            else:

                # Update sand block position
                sand_position = (sand_position[0] - 1, sand_position[1] + 1)
                
        # Make the sand block move to the down
        else:

            # Update sand block position
            sand_position = (sand_position[0], sand_position[1] + 1)
            
    # Compute result for part 2
    result_p2 = fall_sand_block_counter
    
# Print results
print(f"{result_p1 = }")
print(f"{result_p2 = }")