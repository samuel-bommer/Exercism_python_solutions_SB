"""
matching brackets
"""

def is_paired(input_string: str) -> bool:
    """
    Returns a Bool, whether or not brackets match.
    """
    
    dict_brackets = {
        '{' : '}',
        '[' : ']',
        '(' : ')'
    }
    
    brackets = [char for char in input_string if char in ('(', ')', '[',']', '{','}')]
    
    if len(brackets) % 2 == 1:
        return False
    
    open_brackets = []
    for bracket in brackets:
        if bracket in dict_brackets.keys():
            open_brackets.append(bracket)
        
        if open_brackets:
            if dict_brackets[open_brackets[-1]] == bracket:
                open_brackets.pop(-1)
            
    if not open_brackets:
        return True
    
    return False