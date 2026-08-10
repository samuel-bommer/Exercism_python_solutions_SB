"""
ETL
"""

def transform(legacy_data: dict) -> dict:
    """
    Change data ormat of letters and their
    point values in the game
    """

    transformed_dict = {}
    for key, value in legacy_data.items():
        for char in value:
            char_lower = char.lower()
            transformed_dict[char_lower] = key
            
    return transformed_dict