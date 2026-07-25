def is_armstrong_number(number):
    """
    An armstrong number is a number that is the sum of its own digits
    each raised to the power of the number of digits. 
    
    This function determines if a given number is an armstrong number
    """
    
    str_number = str(abs(number))
    num_digits = len(str_number)
    
    sum_of_digits_list = []
    for string in str_number:
        raised = int(string) ** num_digits
        sum_of_digits_list.append(raised)
        
    sum_of_digits = sum(sum_of_digits_list)
    if sum_of_digits == number:
        return True
    return False
