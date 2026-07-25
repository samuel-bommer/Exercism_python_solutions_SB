def square(number):
    """
    Calculates the value on the square defined by number
    """
    
    if number > 64 or number < 1:
        raise ValueError('square must be between 1 and 64')
    num = number - 1
    return 2**num

def total():
    """
    Calculates the total amount of grains on the chessboard
    """
    
    last_square = 2**64
    total_sqr = last_square - 1
    return total_sqr
