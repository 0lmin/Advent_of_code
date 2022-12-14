# Set file to use as input
filename: str = 'input.txt'

# Set dividers signals
divider1: 'list(list(int))' = [[2]]
divider2: 'list(list(int))' = [[6]]

# Create function to compare two signals to determine if they are right ordered or not
def compare_signals(first_signal: 'list(list(...)) | int', 
                    second_signal: 'list(list(...)) | int') -> int:
    """ 
    @Description:
        Return the list of all accessible neighbors of the current position in the height_map

    @Input:
        first_signal:  list(list(...)) | int = First signal to compare
        second_signal: list(list(...)) | int= Second signal to compare

    @Output:
        _: int = Comparison of the 2 lists:
                    -1 => First list is lower than second list
                    0  => Lists are equal
                    1  => First list is higher than second list
    """
    
    # Match each possible type for the two signals
    match [type(first_signal).__name__, type(second_signal).__name__]:
        
        # Exit case with only ints
        case ['int', 'int']:
            return first_signal - second_signal
        
        # Rebuild first signal
        case ['int', 'list']:
            return compare_signals([first_signal], second_signal)
        
        # Rebuild second signal
        case ['list', 'int']:
            return compare_signals(first_signal, [second_signal])
        
        # Parse two lists case
        case ['list', 'list']:
            
            # Iterate through all element of the two list
            for first_signal_elem, second_signal_elem in zip(first_signal, second_signal):
                
                # Compute comparison
                comparison_result = compare_signals(first_signal_elem, second_signal_elem)
                
                # Check if the elements are equal
                if comparison_result:
                                    
                    # Update result with sub comparison result
                    return comparison_result
                    
            # Check length of list if no conflict have been found earlier
            return (len(first_signal) - len(second_signal))
 
# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = [line.rstrip() for line in f]
    
    # Initialize results sum
    result_p1: int = 0
    result_p2: int = 0
        
    # Part 1
    # Iterate through all group of lines to compare
    for iterate_line in range(0, len(lines_list), 3):
            
        # Get first and second signal to compare
        first_signal:  'list(list(...))' = eval(lines_list[iterate_line])
        second_signal: 'list(list(...))' = eval(lines_list[iterate_line + 1])
        
        # Compare the two signals
        is_right_ordered: int = compare_signals(first_signal, second_signal)
        
        # Update result for part if needed
        if is_right_ordered < 0:
            result_p1 += ((iterate_line // 3) + 1)
            
    # Part 2
    # Initialize the index of the dividers
    divider1_index: int = 1
    divider2_index: int = 2
    
    # Iterate through all lines containing a signal
    for line in lines_list:
        
        # Get current signal
        if line != '':
            signal: 'list(list(...))' = eval(line)
        else:
            continue
        
        # Update index of the first divider if necessary
        if compare_signals(signal, divider1) < 0:         
            divider1_index += 1
            
        # Update index of the second divider if necessary
        if compare_signals(signal, divider2) < 0:         
            divider2_index += 1
            
    # Compute result for part 2
    result_p2 = divider1_index * divider2_index
    
# Print results
print(f"{result_p1 = }")
print(f"{result_p2 = }")
