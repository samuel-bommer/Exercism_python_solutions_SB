"""
Exercism Darts
"""

def score(x: int, y: int) -> int:
    """
    Takes x and y coordinates as input and 
    returns the score: int as an output. 
    
    Radius of a circle is given by x^2 + y^2 = r^2
    """
    
    x_sqr = x**2
    y_sqr = y**2
    
    def in_radius(x_sqr_f: int, y_sqr_f: int, radius: int) -> bool:
        """
        Helper function to calculate if a given point
        is inside the radius.
        """
        
        inside_y_sqr = radius**2 - x_sqr_f
        
        if y_sqr_f <= inside_y_sqr:
            return True
        return False
    
    if in_radius(x_sqr, y_sqr, 1):
        return 10
    
    elif in_radius(x_sqr, y_sqr, 5):
        return 5
    
    elif in_radius(x_sqr, y_sqr, 10):
        return 1
    
    return 0