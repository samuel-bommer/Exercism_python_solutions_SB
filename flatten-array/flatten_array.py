"""
flatten array
"""

def flatten(iterable: list[list]) -> list:
    """
    Take a nested array and return a flattened array.
    "null" value will be disregarded.
    """
    
    flat = []
    check = list(iterable)
    
    while len(check) > 0:
        item = check.pop(0)
        if isinstance(item, list):
            check = item + check
        
        elif item in {'null', None}:
            continue
        
        else:
            flat.append(item)
    
    return flat
            