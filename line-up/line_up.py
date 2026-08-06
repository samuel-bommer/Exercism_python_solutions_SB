"""
Line up
"""


def line_up(name: str, number: int) -> str:
    """
    - Numbers ending in 1 (unless ending in 11) → `"st"`
    - Numbers ending in 2 (unless ending in 12) → `"nd"`
    - Numbers ending in 3 (unless ending in 13) → `"rd"`
    - All other numbers → `"th"`
    """
    
    ending = ''
    str_number = str(number)
    number_ending = 0
    if len(str_number) >= 2:
        number_ending = int(str_number[-2] + str_number[-1])
    
    if str_number[-1] == '1' and number_ending != 11:
        ending = 'st'
        
    elif str_number[-1] == '2' and number_ending != 12:
        ending = 'nd'
        
    elif str_number[-1] == '3' and number_ending != 13:
        ending = 'rd'
        
    else:
        ending = 'th'
        
    string_cust = f'{name}, you are the {number}{ending} customer we serve today. Thank you!'
    return string_cust