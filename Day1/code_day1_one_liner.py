filename: str = 'input.txt'

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = f.readlines()
    
# One liner to parse the list of lines and get the result
print(max([sum(list(map(float, lines_list[([-1] + list(map(lambda x: x[0], filter(lambda x: x[1].startswith('\n'), enumerate(lines_list)))))[i] + 1:
                                          ([-1] + list(map(lambda x: x[0], filter(lambda x: x[1].startswith('\n'), enumerate(lines_list)))))[i+1]]))) 
                                                for i in range(len([-1] + list(map(lambda x: x[0], filter(lambda x: x[1].startswith('\n'), enumerate(lines_list))))) - 1)]))
