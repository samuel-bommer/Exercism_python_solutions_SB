"""
Pick the best hand in poker.
- Spades, Hearts, Diamonds, Clubs
"""

VALUES_JKQA = {
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

def analyse_card(hand: list[str]) -> list:
    
    hand_strs = hand[0].split()
    values = []
    suits = []
    for card in hand_strs:
        val = card[:-1]
        suit = card[-1]
        
        values.append(val)
        suits.append(suit)
                
    return values, suits


def four_of_a_kind(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    
    set_num = set(values)
    if len(set_num) == 2:
        return True, values
    return False, None


def royale_flush(hand: list[str]) -> bool: 
    
    values, suits = analyse_card(hand)
    
    if set(values) == {'A', 'K', 'Q', 'J','10'}:
        if len(set(suits)) == 1:
            return True, values
    return False, None

def straight_flush(hand: list[str]) -> bool:
    
    values, suits = analyse_card(hand)
    
    if set(values) == {'J', '10', '9', '8', '7'}:
        if len(set(suits)) == 1:
            return True, values
    return False, None


def full_house(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    
    if len(set(values)) == 2:
        return True, values
    return False, None


def flush(hand: list[str]) -> bool:
    
    values, suits = analyse_card(hand)
    
    if len(set(suits)) == 1:
        return True, values
    return False, None


def straight(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    
    values_num = [VALUES_JKQA.get(num, int(num)) for num in values]
    values_num.sort(reverse=True)
    
    highest_value = values_num[0]
    
    straight_list = []
    for num in range(5):
        val = highest_value - num
        straight_list.append(val)
        
    if values_num == straight_list:
        return True, values
    return False, None
    

def three_of_a_kind(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    
    if len(set(values)) == 3:
        
        seen = set()
        duplicates = []
        for val in values:
            if val in seen:
                duplicates.append(val)
            else:
                seen.add(val)
        
        if len(set(duplicates)) == 1:
            return True, values
    return False, None


def two_pair(hand: list[str]) -> bool:

    values,_ = analyse_card(hand)
    
    if len(set(values)) == 3:
        
        seen = set()
        duplicates = []
        for val in values:
            if val in seen:
                duplicates.append(val)
            else:
                seen.add(val)
        
        if len(set(duplicates)) == 2:
            return True, values
    return False, None


def two_of_a_kind(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    
    if len(set(values)) == 4:
        return True, values
    return False, None


def high_card(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    
    if len(set(values)) == 5:
        return True, values
    return False, None
    
    
RANK_POKERHANDS = {
    10: royale_flush,
    9: straight_flush,
    8: four_of_a_kind,
    7: full_house,
    6: flush,
    5: straight,
    4: three_of_a_kind,
    3: two_pair,
    2: two_of_a_kind,
    1: high_card
}


def check_values(hand: list[str]) -> int:

    values,_ = analyse_card(hand)
    
    values_num = [VALUES_JKQA.get(num, int(num)) for num in values]
    values_num.sort(reverse=True)
    
    highest_value = values_num[0]
    return highest_value
    

def best_hands(hands: list[str]) -> list[str]:
    """
    Pick the best hand from a list of poker hands
    """
    
    best_score = -1
    winning_hands = []
    
    for hand in hands:
        current_hand_score = 0
        
        for rank, check_function in RANK_POKERHANDS.items():
            is_present, values = check_function(hand)
            if is_present:
                current_hand_score = rank
                break
            
        if current_hand_score > best_score:
            best_score = current_hand_score
            