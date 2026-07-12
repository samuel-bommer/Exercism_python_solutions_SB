"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    return list([number, number+1, number+2])

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return list(rounds_1 + rounds_2)

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    return number in rounds

def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    
    sum_val = 0
    for i in hand:
        sum_val += i
    mean_hand = sum_val / len(hand)
    return mean_hand

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    mean_hand = card_average(hand)
    
    #calulate the median value
    
    middle_index = len(sorted(hand)) / 2
    
    if len(hand) // 2:
        median_value = hand[int(middle_index)]
        
    else:
        middle_index_fl = len(sorted(hand)) // 2  
        median_value = (hand[int(middle_index_fl) - 1] + hand[int(middle_index_fl) + 2])
        
    
    first_last_value = [hand[0], hand[-1]]
    approx_mean = card_average(first_last_value)
    
    if median_value == mean_hand or approx_mean == mean_hand:
        return True
    return False
    

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    length_hand = len(hand)
    
    list_index_is_even = []
    list_index_is_odd = []
    
    for i in range(length_hand):
        if i % 2 == 0:
            list_index_is_even.append(i)
        else:
            list_index_is_odd.append(i)
            
    average_even = card_average([hand[i] for i in list_index_is_even])
    average_odd = card_average([hand[i] for i in list_index_is_odd]) 
    
    if average_even == average_odd:
        return True
    return False

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """
    
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
