# Set file to use as input
filename: str = 'input.txt'

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = [line.rstrip() for line in f]
    
    # Initialize results sum
    result_p1: int = 0
    result_p2: int = 0
    
    # Iterate through all lines
    for line in lines_list:
        
        # Iterate through the data stream
        for starting_index, _ in enumerate(line):
            
            # Check if there is a repeated char using set (4-char buffer)
            if not(result_p1) and len(set(line[starting_index - 4 : starting_index])) == 4:
                
                # Set result
                result_p1 = starting_index
            
            # Check if there is a repeated char using set (14-char buffer)
            if len(set(line[starting_index - 14 : starting_index])) == 14:
                
                # Set result
                result_p2 = starting_index
                
            # Check for early break (only need p2 because result_p2 >= result_p1)
            if result_p2:
                break


# Pint results
print(result_p1)
print(result_p2)