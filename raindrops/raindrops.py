def convert(number: int) -> str:
    """
    If a given number is divisible by 3, add "Pling"
    If a given number is divisible by 5, add "Plang"
    If a given number is divisible by 7, add "Plong"
    
    If it is not divisible by the above numbers, the result
    is the given number as a string. 
    Return string.
    """
    
    raindrops = ''
    
    if number % 3 == 0:
        raindrops += 'Pling'
        
    if number % 5 == 0:
        raindrops += 'Plang'
        
    if number % 7 == 0:
        raindrops += 'Plong'
        
    if not raindrops:
        return str(number)
    return raindrops
