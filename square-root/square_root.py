"""
Square root approcimation
"""

def square_root(number: int, epsilon: float=0.001) -> int:
    """
    Calculate the square root of a number 
    using binary search essentially
    """
    
    if number < 0:
        raise ValueError('irrational')
    
    if number == 0:
        return 0
    
    high = number
    low = 0 
    
    while (high - low) > epsilon:
        mid = (low + high) / 2
        mid_sqr = mid * mid
        
        if mid_sqr < number:
            low = mid
            
        else:
            high = mid
            
    
    mid = (low + high) / 2 
    return int(round(mid, 0))