"""
Binary search tree
"""


def middle_val(low: int, high: int) -> int:
    """
    Helper function
    """
    
    index_ = (low + high) // 2
    return index_
    
    
def find(search_list: list, value: int) -> int:
    """
    Binary search algorithm. We continuously
    half the list until we find the location
    """
    
    search_list.sort()
    
    if not bool(search_list):
        raise ValueError('value not in array')
    
    if min(search_list) > value or max(search_list) < value:
        raise ValueError('value not in array')
    
    if not(value in search_list):
        raise ValueError('value not in array')
    
    low = 0
    high = len(search_list)
    index = middle_val(low, high)
    
    while value != search_list[index]:
        if value < search_list[index]:
            high = index
            index = middle_val(low, high)
            
        else:
            low = index
            index = middle_val(low, high)
        
    return index
    
    
    