"""
Resistor color duo
"""

resistor_colors = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

def value(colors: list) -> int:
    """
    Value of two resistor colors
    """
    
    val_list = []
    count = 0
    for col in colors:
        if col in resistor_colors and count < 2:
            value_col = resistor_colors.get(col)
            val_list.append(str(value_col))
            count += 1
    
    string_numbers = ''.join(val_list)
    int_numbers = int(string_numbers)
    
    return int_numbers