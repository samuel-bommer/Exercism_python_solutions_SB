"""
Pangram exercise
"""

def is_pangram(sentence: str) -> bool:
    """
    A pangram contains all the letters
    in the english alphabet (at least once).
    """
    
    sentence_letters = ''
    
    for char in sentence:
        if char.isalpha():
            sentence_letters += char
            
    sentence_set = set(sentence_letters.lower())
    
    if len(sentence_set) == 26:
        return True
    
    return False
    