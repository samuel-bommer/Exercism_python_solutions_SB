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
    
    hand_strs = hand.split()
    values = []
    suits = []
    for card in hand_strs:
        val = card[:-1]
        suit = card[-1]
        
        values.append(val)
        suits.append(suit)
                
    return values, suits


def get_numeric_rank(hand: list[str]) -> list[int]:

    values,_ = analyse_card(hand)
    
    values_num = [VALUES_JKQA[num] if num in VALUES_JKQA else int(num) for num in values]
    values_num.sort(reverse=True)
    
    return values_num


def four_of_a_kind(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    ranks = get_numeric_rank(hand)
    
    set_num = set(values)
    if len(set_num) == 2 and (ranks[0] == ranks[3] or ranks[1] == ranks[4]):
        quad = ranks[2]
        
        card_counts = {}
        for card in ranks:
            card_counts[card] = card_counts.get(card, 0) + 1
        
        kicker = [card for card in card_counts if card_counts[card] == 1]
        
        return True, [quad, kicker]
    return False, 0


def royale_flush(hand: list[str]) -> bool: 
    
    values, suits = analyse_card(hand)
    
    if set(values) == {'A', 'K', 'Q', 'J','10'}:
        if len(set(suits)) == 1:
            return True, 14
    return False, 0


def straight_flush(hand: list[str]) -> bool:
    
    _, suits = analyse_card(hand)
    values_num = get_numeric_rank(hand)
    
    if len(set(suits)) != 1:
        return False, 0
    
    if values_num == [14, 5, 4, 3, 2]:
        return True, 5
    
    highest_value = values_num[0]
    expected = list(range(highest_value, highest_value - 5, -1))
    if values_num == expected:
        return True, highest_value
    
    return False, 0


def full_house(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    ranks = get_numeric_rank(hand)
    
    
    if len(set(values)) == 2:
        card_counts = {}
        for card in ranks:
            card_counts[card] = card_counts.get(card, 0) + 1
        
        triplets = [card for card in card_counts if card_counts[card] == 3]
        pair = [card for card in card_counts if card_counts[card] == 2]
        
        return True, [triplets, pair]
    return False, 0


def flush(hand: list[str]) -> bool:
    
    _, suits = analyse_card(hand)
    ranks = get_numeric_rank(hand)
    
    if len(set(suits)) == 1:
        return True, ranks
    return False, 0


def straight(hand: list[str]) -> bool:
    
    values_num = get_numeric_rank(hand)
    
    highest_value = values_num[0]
    
    straight_list = []
    for num in range(5):
        val = highest_value - num
        straight_list.append(val)
        
    if values_num == straight_list:
        return True, highest_value
    
    if values_num == [14, 5, 4, 3, 2]:
        return True, 5
    
    return False, 0
    

def three_of_a_kind(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    ranks = get_numeric_rank(hand)
    
    if len(set(values)) == 3:
        
        seen = set()
        duplicates = []
        for val in values:
            if val in seen:
                duplicates.append(val)
            else:
                seen.add(val)
        
        if len(set(duplicates)) == 1:
            thruple = [rank for rank in set(ranks) if ranks.count(rank) == 3]
            kickers = [card for card in ranks if card not in thruple]
            return True, [thruple, *kickers]
    return False, 0


def two_pair(hand: list[str]) -> bool:

    values,_ = analyse_card(hand)
    ranks = get_numeric_rank(hand)
    
    if len(set(values)) == 3:
        
        card_counts = {}
        for card in ranks:
            card_counts[card] = card_counts.get(card, 0) + 1
        
        pairs = sorted([card for card in card_counts if card_counts[card] == 2], reverse=True)
        
        if len(set(pairs)) == 2:
            kicker = [card for card in card_counts if card_counts[card] == 1]
            return True, [pairs[0], pairs[1], kicker]
        
    return False, None


def two_of_a_kind(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    ranks = get_numeric_rank(hand)
    
    if len(set(values)) == 4:
        pair = [rank for rank in set(ranks) if ranks.count(rank) == 2]
        kickers = [card for card in ranks if card not in pair]
        return True, [*pair, *kickers]
    return False, None


def high_card(hand: list[str]) -> bool:
    
    values,_ = analyse_card(hand)
    ranks = get_numeric_rank(hand)
    
    if len(set(values)) == 5:
        return True, ranks
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
    

def best_hands(hands: list[str]) -> list[str]:
    """
    Pick the best hand from a list of poker hands
    """
    
    best_score = (-1, [])
    winning_hands = []
    
    for hand in hands:
        current_hand_score = (0, [])
        
        for rank, check_function in RANK_POKERHANDS.items():
            is_present, tie_breaker_val = check_function(hand)
            if is_present:
                current_hand_score = (rank, tie_breaker_val)
                break
            
        if current_hand_score > best_score:
            best_score = current_hand_score
            winning_hands = [hand]
        
        elif current_hand_score == best_score:
            winning_hands.append(hand)
                
        
    return winning_hands
        
            
            