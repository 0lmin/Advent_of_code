# Set file to use as input
filename: str = 'input.txt'

# Set all the trigger cycle number
trigger_cycles_list: 'list(int)' = [20, 60, 100, 140, 180, 220]

# Set line width
line_width: int = 40

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = [line.rstrip() for line in f]
    
    # Initialize results sum
    result_p1: int = 0
    result_p2: str = ''
    
    # Initialize cycle count
    cycle_count: int = 0
    
    # Initialize the signal value
    signal_value: int = 1
    
    # Iterate through each lines
    for line in lines_list:
        
        # Match the current command
        match line.split(' '):
            case ["noop"]: 
                
                # Update result for part 2
                result_p2 += '#' if (cycle_count % line_width) in [signal_value - 1, signal_value, signal_value + 1] else '.'
                
                # Count one cycle and do nothing
                cycle_count += 1
                
                # Handle new line
                if cycle_count % line_width == 0:
                    result_p2 += "\n"
                
                # Check if the current cycle is a trigger cycle
                if cycle_count + 1 in trigger_cycles_list:
                    
                    # Add current signal strength
                    result_p1 += ((cycle_count + 1) * signal_value)
                
            case ["addx", value_string]:
                
                # Compute value to add to the signal
                value = int(value_string)
                
                # Update result for part 2
                result_p2 += '#' if (cycle_count % line_width) in [signal_value - 1, signal_value, signal_value + 1] else '.'
                
                # Count one cycle and do nothing
                cycle_count += 1
                
                # Handle new line
                if cycle_count % line_width == 0:
                    result_p2 += "\n"
                
                # Check if the current cycle is a trigger cycle
                if cycle_count + 1 in trigger_cycles_list:
                    
                    # Add current signal strength
                    result_p1 += ((cycle_count + 1) * signal_value)
                    
                # Update result for part 2
                result_p2 += '#' if (cycle_count % line_width) in [signal_value - 1, signal_value, signal_value + 1] else '.'
                
                # Count one cycle and do nothing
                cycle_count += 1
                
                # Handle new line
                if cycle_count % line_width == 0:
                    result_p2 += "\n"
                    
                # Update signal value
                signal_value += value
                
                # Check if the current cycle is a trigger cycle
                if cycle_count + 1 in trigger_cycles_list:
                    
                    # Add current signal strength
                    result_p1 += ((cycle_count + 1) * signal_value)
                                       
# Print results
print(f"{result_p1 = }")
print(result_p2)