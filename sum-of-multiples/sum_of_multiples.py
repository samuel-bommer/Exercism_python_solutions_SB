"""
Sum of multiples
"""

def sum_of_multiples(limit: int, multiples: list) -> int:
    """
    Finds the sum of unique multiples in a given limit.
    """
    
    list_of_multiples = []
    for multi in multiples:
        n = 1
        while n*multi < limit:
            mul = n*multi
            list_of_multiples.append(mul)
            n += 1
            
    sum_multiples_set = set(list_of_multiples)
    sum_multiples = sum(sum_multiples_set)
    return sum_multiples
            
