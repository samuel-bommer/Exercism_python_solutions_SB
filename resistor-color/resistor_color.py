"""
Resistor Color exercise
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

def color_code(color: str) -> int | None:
    """
    Dict with band colors. 
    Output: color code
    """

    if color in resistor_colors:
        return resistor_colors.get(color)
    
    return None

def colors() -> list:
    """
    List of all colors
    """
    
    list_colors = []
    for key in resistor_colors:
        list_colors.append(key)

    return list_colors