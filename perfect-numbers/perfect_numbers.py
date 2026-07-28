"""
Perfect Numbers 
"""


def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    
    divisors = []
    for num in range(1, number):
        if number % num == 0:
            divisors.append(num)
            
    sum_div = sum(divisors)
    
    if sum_div > number:
        return 'abundant'
    
    if sum_div < number:
        return 'deficient'
    
    return 'perfect'