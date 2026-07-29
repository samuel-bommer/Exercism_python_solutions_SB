"""
ISBN verifier
"""


def is_valid(isbn: str) -> bool:
    """
    Check if the ISBN is valid
    """
    
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    
    summing_up = 0
    
    for index, num in enumerate(isbn):
        multi = 10 - index
        if num.isalpha():
            if num == 'X' and index == 9:
                num = 10
            else:
                return False
        num = int(num)
        
        summing_up += num * multi
        
    if summing_up % 11 == 0:
        return True
    
    return False
        
