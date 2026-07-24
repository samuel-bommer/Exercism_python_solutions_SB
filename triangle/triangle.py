def check_invalid_triangle(sides):
    """
    Helper function to check if we have a valid triangle
    """
    
    hypothenuse = sides.index(max(sides))
    catheti = sides.copy()
    catheti.pop(hypothenuse)
    if sum(catheti) < sides[hypothenuse]:
        return True
    
    for side in sides:
        if side == 0:
            return True
    return None

def equilateral(sides):
    """
    Triangle has all three sides the same length
    """
    
    if check_invalid_triangle(sides):
        return False

    if len(set(sides)) == 1:
        return True
    return False

def isosceles(sides):
    """
    Triangle has at least two sides with the same length
    """
    if check_invalid_triangle(sides):
        return False
    
    if len(set(sides)) == 2 or len(set(sides)) == 1:
        return True
    return False

def scalene(sides):
    """
    Triangle has all sides of different length
    """
    if check_invalid_triangle(sides):
        return False

    if len(set(sides)) == 3:
        return True
    return False
