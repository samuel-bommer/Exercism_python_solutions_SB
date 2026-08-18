"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'sublist'
SUPERLIST = 'superlist'
EQUAL = 'equal'
UNEQUAL = 'unequal'


def sublist(list_one: list, list_two: list) -> bool:
    """
    Determine if lists are equal, sublist, or superlist
    """
    
    if len(list_one) == len(list_two):
        if not list_one or not list_two:
            return EQUAL
        
        for index, item in enumerate(list_one):
            if item != list_two[index]:
                return UNEQUAL
            
        if list_one == list_two: 
            return EQUAL
                
    else:
        
        if not list_one:
            return SUBLIST
        
        elif not list_two:
            return SUPERLIST
        
        elif len(list_one) > len(list_two):
            for index, item in enumerate(list_one):
                if list_one[index] == list_two[0]:
                    len_check = len(list_two)
                    if list_one[index:index+len_check] == list_two:
                        return SUPERLIST
            return UNEQUAL
                    
        else:
            for index, item in enumerate(list_two):
                if list_two[index] == list_one[0]:
                    len_check_again = len(list_one)
                    if list_two[index:index+len_check_again] == list_one:
                        return SUBLIST
            return UNEQUAL