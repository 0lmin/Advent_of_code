# -*- coding: utf-8 -*-
"""
Created on Dec 02 2023

Last major update on Dec 02 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 2's challenge of the Advent of Code (AoC) 2023
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List, Dict

################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":
    
    # Set file to use as input
    filename: str = '2023/Day02/input.txt'
    
    # Initialize results
    result_p1: int = 0
    result_p2: int = 0

    # Define the reference bag content for part 1
    reference_bag_dict: Dict[str, int] = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = list(map(lambda line: line.replace("\n", ""), f.readlines()))
        
        # Iterate through lines
        line: str
        for line in lines_list:
            
            # Initialize the current possible bag content
            current_bag_content_dict: Dict[str, int] = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            
            # Retrieve the game number
            game_id: int = int(line.split(":")[0].replace("Game ", ""))
            
            # Clean the line to get the game sets
            game_sets: List[str] = line.split(":")[-1].split(";")
            
            # Iterate through all game sets
            game_set: str
            for game_set in game_sets:
                
                # Split each color
                set_colors: List[str] = game_set.split(",")
                
                # Iterate through each picked color
                set_color: str
                for set_color in set_colors:
                    
                    # Get the color and the count
                    count_str: str
                    color: str
                    _, count_str, color = set_color.split(" ")
                    
                    # Update the current bag content dict
                    current_bag_content_dict[color] = max(current_bag_content_dict[color], int(count_str))
                    
            # Check if the current bag can be the reference bag
            if (current_bag_content_dict["red"] <= reference_bag_dict["red"] and 
                current_bag_content_dict["green"] <= reference_bag_dict["green"] and 
                current_bag_content_dict["blue"] <= reference_bag_dict["blue"]):
                
                # Update the result of part 1
                result_p1 += game_id
                
            # Compute the power of the current bag
            power: int = current_bag_content_dict["red"] * current_bag_content_dict["green"] * current_bag_content_dict["blue"]
            
            # Update the the result of part 2
            result_p2 += power
            
    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")
