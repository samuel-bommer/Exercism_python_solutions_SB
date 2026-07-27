def response(hey_bob):
    """
    Bob's response.
    """
    
    hey_bob = hey_bob.strip()
    
    check = any(char.isalpha() for char in hey_bob)
    non_empty = bool(hey_bob) == True
    
    if check and hey_bob == hey_bob.upper() and non_empty and hey_bob[-1] == '?':
        return 'Calm down, I know what I\'m doing!'
    
    elif non_empty and hey_bob.strip()[-1] == '?':
        return 'Sure.'
    
    elif not non_empty:
        return 'Fine. Be that way!'
    
    elif check and hey_bob == hey_bob.upper() and non_empty:
        return 'Whoa, chill out!'
    
    return 'Whatever.'