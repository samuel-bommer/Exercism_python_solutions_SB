"""
matching brackets
"""


def is_paired(input_string: str) -> bool:
    """
    Returns a Bool, whether or not brackets match.
    """
    
    brackets_string = [for char in input_string in ('(', ')', '[',']', '{','}')]
    for index, bracket in enumerate(brackets_string):
        pass