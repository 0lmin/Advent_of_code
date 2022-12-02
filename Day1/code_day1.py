# Set file to use as input
filename: str = 'input.txt'

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = f.readlines()
    
    # Initialize list of elves carry
    elves_carry_list: 'list(float)' = [0]
    
    # Iterate through lines
    for line in lines_list:
        # Create a new elves
        if line == '\n':
            elves_carry_list.append(0)
        # Add new carry for current elves
        else:
            elves_carry_list[-1] += float(line)
           
    # Get max carried 
    result: float = max(elves_carry_list)
    
    # Print result
    print(result)