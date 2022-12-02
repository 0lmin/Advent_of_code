# Set file to use as input
filename: str = 'input.txt'

# Create correspondence matrix to get a single value for each possible choice
correspondence_dict_p1 = {
    'X': 'A', # Rock
    'Y': 'B', # Paper
    'Z': 'C'  # Scissors
}

correspondence_dict_p2 = {
    'X': -1, # Loose
    'Y': 0,  # Draw
    'Z': 1   # Win
}

def areYouWinningSon_p1(opponent: str, player: str) -> int:
    """
    @Description:
        Return the points gained during the battle with strategy in part 1

    @Input:
        opponent: str = Choice made by the opponent for the battle
        player:   str = Choice made by the player for the battle

    @Output:
        is_winning: bool = points gained during the battle
    """
    
    # Get index in correspondence dict of both choices
    opponent_choice = list(correspondence_dict_p1.values()).index(opponent)
    player_choice   = list(correspondence_dict_p1.values()).index(correspondence_dict_p1[player])
    
    # Detect equality
    if opponent_choice == player_choice:
        return 3 + (player_choice + 1)
    
    # Get winner
    if (opponent_choice + 1) % 3 == player_choice:
        return 6 + (player_choice + 1)
    else:
        return 0 + (player_choice + 1)

def areYouWinningSon_p2(opponent: str, player: str) -> int:
    """
    @Description:
        Return the points gained during the battle with strategy in part 2

    @Input:
        opponent: str = Choice made by the opponent for the battle
        player:   str = Choice made by the player for the battle

    @Output:
        is_winning: bool = points gained during the battle
    """
    
    # Compute
    opponent_choice = list(correspondence_dict_p1.values()).index(opponent)
    player_choice   = (opponent_choice + correspondence_dict_p2[player]) % 3
    
    # Detect equality
    if opponent_choice == player_choice:
        return 3 + (player_choice + 1)
    
    # Get winner
    if (opponent_choice + 1) % 3 == player_choice:
        return 6 + (player_choice + 1)
    else:
        return 0 + (player_choice + 1)

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = f.readlines()
    
    # Initialize results sum
    result_p1: int = 0
    result_p2: int = 0
    
    # Iterate through lines
    for line in lines_list:
        result_p1 += areYouWinningSon_p1(line[0], line[2])
        result_p2 += areYouWinningSon_p2(line[0], line[2])
        
# Pint results
print(result_p1)
print(result_p2)