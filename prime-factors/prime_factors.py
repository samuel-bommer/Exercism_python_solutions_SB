"""
Compute the prime factors of a given natural number.

As we know, a prime number is only evenly divisible by itsef and 1.
"""

def factors(value: int) -> list[int]:
    """
    Input: int value
    Output: list of prime factors
    """

    prime_factors = []

    while value % 2 == 0:
        value //= 2
        prime_factors.append(2)

    while value % 3 == 0:
        value //= 3
        prime_factors.append(3)

    factor = 5
    while factor * factor <=value:
        while value % factor == 0:
            value //= factor
            prime_factors.append(factor)
        factor += 2
    
    if value > 1:
        prime_factors.append(value)

    return prime_factors

