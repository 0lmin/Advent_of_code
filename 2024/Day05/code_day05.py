# -*- coding: utf-8 -*-
"""
Created on Dec 05 2024

Last major update on Dec 05 2024

@author: BERTIN Clément (0lmin)
 
Description:
Advent of Code (AoC) 2024 day 05
"""

################################################################################
################################ Imports #######################################
################################################################################

# Import StingIO class for typing
from io import StringIO

# Import typing utils
from typing import List, Dict, Set, Tuple

################################################################################
############################## Functions #######################################
################################################################################

def isUpdateCorrect(update: List[int]) -> Tuple[bool, int, Set[int]]:
    # Initialize the set of seen page
    seen_page: Set[int] = set()
    
    # Initialize the flag for correctness of the update
    is_correct: bool = True
    
    # Iterate through the current update
    iterate_page: int
    page: int
    for iterate_page, page in enumerate(update):
        
        # Check if a rule correspond to the page
        if page in page_with_rule_list:
            
            # Get the set of page that must not be before the current page
            page_after_set: Set[int] = rules_dict[page]
            
            # Check if any rule is broken
            if page_after_set.intersection(seen_page) != set():
                
                # Update the flag of correctness
                is_correct = False
                
                # Early break because the update is not correct
                break                    
            
        # Add the seen page in the set
        seen_page.add(page)
        
    return is_correct, iterate_page, page_after_set.intersection(seen_page)

################################################################################
################################# Main #########################################
################################################################################

if __name__ == "__main__":
    
    # Set file to use as input
    filename: str = "2024/Day05/input.txt"

    # Get file content
    f: StringIO
    with open(filename) as f:
        
        # Read all lines
        lines_list: List[str] = list(map(lambda line: line.replace("\n", ""), f.readlines()))
        
        # Split between rules and updates
        rule_line_list: List[str] = lines_list[:lines_list.index('')]
        update_line_list: List[List[int]] = list(map(lambda line: list(map(int, line.split(","))), lines_list[lines_list.index('') + 1:]))
        
        # Store the rules inside a dictionary
        rules_dict: Dict[int, Set[int]] = {before: set() for before, _ in [list(map(int, rule.split("|"))) for rule in rule_line_list]}
        
        # Fill the rules' dict
        before: int
        after: int
        for before, after in [list(map(int, rule.split("|"))) for rule in rule_line_list]:
            
            # Add the current value to be after
            rules_dict[before].add(after)
            
        # Compute the list of page for which a rule exist
        page_with_rule_list: List[int] = list(rules_dict.keys())
        
        # Initialize the list of incorrect updates
        incorrect_update_list: List[List[int]] = []
        
        # Initialize the result of part 1
        result_p1: int = 0
        
        # Initialize the result of part 2
        result_p2: int = 0
            
        # Iterate through all updates
        update: List[int]
        for update in update_line_list:
            
            is_correct: bool = isUpdateCorrect(update)[0]
                
            # Update teh result if needed
            if is_correct:
                result_p1 += update[len(update)//2]
                
            # Add them in the incorrect updates
            else:
                incorrect_update_list.append(update)
                
        # Iterate the incorrect update to fix them
        incorrect_update: List[int]
        for incorrect_update in incorrect_update_list[0:]:
            
            # Initialize the status of the update
            update_status: bool = False
            
            # Initialize the detected incorrect pages
            incorrect_page_before_index: int
            pages_after: Set[int]
            _, incorrect_page_before_index, pages_after = isUpdateCorrect(incorrect_update)
            
            # Iterate through the pages until the update is correct
            while not(update_status):
                
                # Find the index of the first page that should come after
                first_wrong_after_page_index: int = min([incorrect_update.index(page) for page in pages_after])
                
                # Update the incorrect_update to try solving the issue
                incorrect_update = incorrect_update[:first_wrong_after_page_index] + \
                                    [incorrect_update[incorrect_page_before_index]] + \
                                    incorrect_update[first_wrong_after_page_index:incorrect_page_before_index] + \
                                    incorrect_update[incorrect_page_before_index + 1:]
                               
                # Update the status and the incorrect pages of the update after modification
                update_status, incorrect_page_before_index, pages_after = isUpdateCorrect(incorrect_update)
                            
            # Update the result of part 2 after fix
            result_p2 += incorrect_update[len(incorrect_update)//2]
            
        # Print results
        print(f"{result_p1 = }")
        print(f"{result_p2 = }")