# Import deepcopy
from copy import deepcopy

# Set file to use as input
filename: str = 'input.txt'

def get_starting_position(position_list: 'list(str)') -> 'list(str)':
    """
    @Description:
        Return a list of stack (list) corresponding to the starting position 

    @Input:
        position_list: list(list(str)) = List of all the positions at the start

    @Output:
        starting_position: list(list(str)) = Starting position represented as a list of
                                             list (stack) for each column
    """
    
    # Create empty position
    nb_stack: int = len(position_list[-1].split('  '))
    starting_position: 'list(str)' = [[] for _ in range(nb_stack)]
    
    # Remove axis
    position_list = position_list[:-1]
       
    # Iterate through all lines of the reversed list of lines
    for line in position_list[::-1]:

        # Iterate through current line 4 by 4
        for stack_index, content_index in enumerate(range(0, len(line), 4)):
            
            # Get current content
            content: str = line[content_index:(content_index + 4)]
            
            # Add in stack if needed
            if content != '    ':
                starting_position[stack_index].append(content[1])
                
    # Return list of stack at starting position
    return starting_position

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = [line.rstrip() for line in f]
    
    # Initialize results sum
    result_p1: str
    result_p2: str
    
    # Get separation between position and move
    separation_index: int = lines_list[:-1].index('')
    
    # Separate move and starting position
    position_p1: 'list(str)' = get_starting_position(lines_list[:separation_index])
    position_p2: 'list(str)' = deepcopy(position_p1)
    
    # Remove starting position to only get moves
    moves_list: 'list(str)' = lines_list[separation_index+1:]
    
    # Iterate through moves
    for move in moves_list:
        
        # Get destination stack
        destination_stack_index: int = int(move.split(' to ')[-1]) - 1
        move = move.split(' to ')[0]

        # Get origin stack
        origin_stack_index: int = int(move.split(' from ')[-1]) - 1
        move = move.split(' from ')[0]
        
        # Get number of move
        nb_move: int = int(move.split('move ')[-1])
        
        # Apply moves for this line for part 1
        for _ in range(nb_move):
            position_p1[destination_stack_index].append(position_p1[origin_stack_index].pop())
            
        # Apply moves for this line for part 2
        position_p2[destination_stack_index] += position_p2[origin_stack_index][-nb_move:]
        position_p2[origin_stack_index] = position_p2[origin_stack_index][:-nb_move]
            
    # Compute result_p1 after all moves
    result_p1 = ''.join([stack[-1] for stack in position_p1])
    result_p2 = ''.join([stack[-1] for stack in position_p2])

# Pint results
print(result_p1)
print(result_p2)