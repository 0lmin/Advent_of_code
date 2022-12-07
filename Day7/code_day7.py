# Set file to use as input
filename: str = 'input.txt'

# Set maximal size for accepted dir
max_dir_size: int = 100_000

# Set total disk space
total_disk_space: int = 70_000_000

# Set needed space
needed_space: int = 30_000_000

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = [line.rstrip() for line in f]
    
    # Initialize results sum
    result_p1: int = 0
    result_p2: int = 0
    
    # Initialize dictionary of directories: dir: size
    dir_size: dict = {'/': 0}
    
    # Initialize directory parent dictionary
    dir_parents: dict = {'/': []}
    
    # Initialize the directory stack
    dir_stack: 'list(str)' = ['/']
    
    # Initialized total used size variable
    total_used_space: int = 0
    
    # Iterate through all lines
    for line in lines_list:
        
        # Match case for each case
        match line.split(' '):
            
            # Go to previous directory
            case ["$", "cd", '..']:
                dir_stack.pop()
                
            # Restart to root directory
            case ["$", "cd", '/']:
                dir_stack = ['/']
                
            # Move to next directory
            case ["$", "cd", destination_dir]:
                
                # Compute full path of the file
                file_path: str = '/'.join(dir_stack[1:] + [destination_dir])
                                     
                # Add it in the stack
                dir_stack.append(file_path)
                
            # Add directory in the dictionary of directories and in directory parents dictionary
            case ["dir", dir_name]:
                # Compute full path of the file
                file_path: str = '/'.join(dir_stack[1:] + [dir_name])
                
                # Add it in the size dictionary
                dir_size['/'.join(dir_stack[1:] + [dir_name])] = 0
        
            case [size, filename] if size != "$":
                
                # Update size of all the directories in the stack
                for dir in dir_stack:
                    dir_size[dir] += int(size)
                    
                # Update total used size
                total_used_space += int(size)

    # Sum size of all directories with size less than max_dir_size
    result_p1 = sum(filter(lambda x: x <= max_dir_size, dir_size.values()))
    
    # Get total size to free
    size_to_free = total_used_space - (total_disk_space - needed_space)
    
    # Get size of the smallest directory that can leave enough space for the update
    result_p2 = min(filter(lambda x: x >= size_to_free, dir_size.values()))
    
# Print results
print(f"{result_p1 = }")
print(f"{result_p2 = }")