def leap_year(year):
    """
    A leap year occurs in every year that is evenly 
    divisivle by 4, unless the year is evenly divisible
    by 100 where it is only a leap year if it is also evenly
    divisible by 400.
    
    This function takes int: year and evaluates if the given
    year was a leap year or not.
    
    Returns Boolean: True if it is a leap year
    """
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    
    return False
            
    
    
