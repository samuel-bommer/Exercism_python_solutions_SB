"""
Diamond Exercise: The diamond kata takes as its input a letter, and outputs
it in a diamond shape. Given a letter, it prints a diamond starting with 'A'.
"""

import string
UPPER_ALPHABET = string.ascii_uppercase

def rows(letter: str) -> str:
    """
    Prints the rows of the diamond. Takes in a letter as a string and 
    loops through the alphabet until that letter appears and then does
    the reverse to construct the diamond
    """
    
    diamond_letters = []
    for char in UPPER_ALPHABET:
        if char != letter:
            diamond_letters.append(char)
        else:
            break
    
    diamond_letters.append(letter)
    
    upper_limit = 26*2
    uneven_numbers = [char for char in range(upper_limit) if char %2 != 0]
    
    
    diamond_upper = []
    
    index_of_letter = diamond_letters.index(letter)
    max_number_of_spaces = uneven_numbers[index_of_letter]
    
    mid_indx = int((max_number_of_spaces - 1) / 2)
    lower_index = mid_indx
    upper_index = mid_indx
        
    for char in diamond_letters:
        list_row = list(max_number_of_spaces * ' ')
        
        list_row[lower_index] = char
        list_row[upper_index] = char
        
        row = ''.join(list_row)
        diamond_upper.append(row)
        
        lower_index -= 1
        upper_index += 1
        
    diamond_lower = []
    for indx, row in enumerate(reversed(diamond_upper)):
        
        if indx == 0:
            continue
        
        diamond_lower.append(row)
    
    
    diamond = diamond_upper + diamond_lower
    
    return diamond
    
    
        
