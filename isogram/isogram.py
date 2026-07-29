"""
Isogram exercise
"""

def is_isogram(phrase: str) -> bool:
    """
    Check if a phrase is an isogram (no repeating letters)
    """
    
    alpha_phrase = ''
    for char in phrase:
        if char.isalpha():
            alpha_phrase += char
            
    if len(set(alpha_phrase.lower())) == len(alpha_phrase.lower()):
        return True
    
    return False
