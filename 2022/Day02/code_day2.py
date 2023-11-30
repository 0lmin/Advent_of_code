# -*- coding: utf-8 -*-
"""
Created on Dec 02 2022

Last major update on Nov 30 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 2's challenge of the Advent of Code (AoC)
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List, Dict

################################################################################
############################# Configuration ####################################
################################################################################

# Create correspondence matrix to get a single value for each possible choice
_correspondence_dict_p1: Dict[str, str] = {
    'X': 'A', # Rock
    'Y': 'B', # Paper
    'Z': 'C'  # Scissors
}

_correspondence_dict_p2: Dict[str, int] = {
    'X': -1, # Loose
    'Y': 0,  # Draw
    'Z': 1   # Win
}

################################################################################
############################### Function #######################################
################################################################################

def areYouWinningSon_p1(opponent: str, 
                        player: str) -> int:
    """
    @Description:
        Compute the points gained during the battle with strategy in part 1

    @Input:
        - opponent:
            Choice made by the opponent for the battle
        - player:
            Choice made by the player for the battle

    @Output:
        - _:
            Points gained during the battle
    """
    
    # Get index in correspondence dict for both choices
    opponent_choice: int = list(_correspondence_dict_p1.values()).index(opponent)
    player_choice: int = list(_correspondence_dict_p1.values()).index(_correspondence_dict_p1[player])
    
    # Detect equality
    if opponent_choice == player_choice:
        return 3 + (player_choice + 1)
    
    # Get winner
    if (opponent_choice + 1) % 3 == player_choice:
        return 6 + (player_choice + 1)
    else:
        return 0 + (player_choice + 1)

def areYouWinningSon_p2(opponent: str, 
                        player: str) -> int:
    """
    @Description:
        Compute the points gained during the battle with strategy in part 2

    @Input:
        - opponent:
            Choice made by the opponent for the battle
        - player:
            Choice made by the player for the battle

    @Output:
        - _:
            Points gained during the battle
    """
    
    # Get index in correspondence dict for both choices
    opponent_choice: int = list(_correspondence_dict_p1.values()).index(opponent)
    player_choice: int = (opponent_choice + _correspondence_dict_p2[player]) % 3
    
    # Detect equality
    if opponent_choice == player_choice:
        return 3 + (player_choice + 1)
    
    # Get winner
    if (opponent_choice + 1) % 3 == player_choice:
        return 6 + (player_choice + 1)
    else:
        return 0 + (player_choice + 1)

################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":

    # Set file to use as input
    filename: str = '2022/Day02/input.txt'

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = f.readlines()
        
        # Initialize results sum
        result_p1: int = 0
        result_p2: int = 0
        
        # Iterate through lines
        line: str
        for line in lines_list:
            result_p1 += areYouWinningSon_p1(line[0], line[2])
            result_p2 += areYouWinningSon_p2(line[0], line[2])
            
    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")