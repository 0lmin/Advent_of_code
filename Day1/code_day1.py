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
           
    # Get results
    result_p1: float = max(elves_carry_list)
    result_p2: float = sum(sorted(elves_carry_list)[-3:])
    
# Print results
print(f"{result_p1 = }")
print(f"{result_p2 = }")