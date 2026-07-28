"""
Reverse string
"""

def reverse(text: str) -> str:
    """
    reversing a string
    """
    
    rev_string = ''
    for char in text[::-1]:
        rev_string += char
        
    return rev_string