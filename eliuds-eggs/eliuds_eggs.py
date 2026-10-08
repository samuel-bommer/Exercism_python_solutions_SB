def egg_count(display_value: int) -> int:
    """
    The function counts the eggs in the basket: we transform
    a integer into binary and then count the amount of 1 to get
    the number of eggs. 
    """
    if display_value == 0:
        return 0
    
    remainder_binary = []
    while display_value > 0:
        remainder = display_value % 2
        remainder_binary.append(remainder)
        
        display_value = display_value // 2
    
    egg_count = remainder_binary.count(1)
    return egg_count
        
