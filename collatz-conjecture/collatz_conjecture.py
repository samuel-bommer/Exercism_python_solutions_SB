def steps(number):
    """
    Collatz conjecture: can every number find to 1? 
    The rules for this puzzle are: 
    - If the number is even, divide by 2
    - If the number is odd, divide by 3 and add 1
    Then we would repeat until we reach 1.
    
    This function does exactly that with some input number, returning
    the number of steps until 1 is reached.
    """
    
    if number <= 0:
        raise ValueError('Only positive integers are allowed')
    
    count = 0
    
    while number > 1:
        if number % 2 == 0:
            number = number / 2
            count += 1
        else:
            number = number * 3 + 1
            count += 1
    return count