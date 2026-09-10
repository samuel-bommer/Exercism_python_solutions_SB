"""
Pick the best hand in poker.
- Spades, Hearts, Diamonds, Clubs
"""

def analyse_card(hand: list[str]) -> list:
    
    hand_strs = hand[0].split()
    values = []
    suits = []
    for card in hand_strs:
        val = card[0]
        suit = card[1]
        
        values.append(val)
        suits.append(suit)
                
    return values, suits


def four_of_a_kind(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    
    set_num = set(values)
    if len(set_num) == 2:
        return True
    return False

def royale_flush(hand: list[str]) -> bool: 
    
    values, suits = analyse_card(hand)
    
    if set(values) == {'A', 'K', 'Q', 'J','10'}:
        if len(set(suits)) == 1:
            return True
    return False

def straight_flush(hand: list[str]) -> bool:
    
    values, suits = analyse_card(hand)
    
    
    


def best_hands(hands: list[str]) -> list[str]:
    """
    Pick the best hand from a list of poker hands
    """
    pass