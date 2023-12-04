# -*- coding: utf-8 -*-
"""
Created on Dec 04 2023

Last major update on Dec 04 2023

@author: BERTIN Clément (0lmin)
 
Description:
Day 4's challenge of the Advent of Code (AoC) 2023
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
    filename: str = '2023/Day04/input.txt'
    
    # Initialize results
    result_p1: int = 0
    result_p2: int = 0

    # Get file content
    f: StringIO
    with open(filename) as f:
        lines_list: List[str] = list(map(lambda line: line.replace("\n", ""), f.readlines()))
        
        # Initialize the storage of won card
        won_card: Dict[int, int] = dict()
        
        # Iterate through lines
        iterate_line: int
        line: str
        for iterate_line, line in enumerate(lines_list):
            
            # Update the count of this card
            won_card[iterate_line] = won_card.get(iterate_line, 0) + 1
                        
            # Clean header of the line
            line = line.split(": ")[-1]
            
            # Split between winning number and number we have
            winning_number: List[int]
            having_number: List[int]
            winning_number, having_number = list(map(lambda l: list(map(int, [val for val in l.split(" ") if val != ""])), line.split(" | ")))
            
            # Initialize the exponent to get the reward
            exponent: int = -1
            
            # Iterate through having number
            number: int
            for number in having_number:
                
                # Check if it is a winning number
                if number in winning_number:
                    
                    # Update the exponent to compute the reward
                    exponent += 1
                    
            # Update result of part 1
            result_p1 += 2 ** exponent if exponent >= 0 else 0
            
            # Get the number of this card
            this_card_count: int = won_card[iterate_line]
            
            # Compute the list of won card
            this_won_card: List[int] = [iterate_line + 1 + val for val in range(exponent + 1)]
            
            # Iterate through the won card
            for card in this_won_card:
                
                # Update the count of won card of this kind
                won_card[card] = won_card.get(card, 0) + this_card_count
                
        # Compute the result of part 2
        result_p2 = sum(won_card.values())
            
    # Print results
    print(f"{result_p1 = }")
    print(f"{result_p2 = }")
