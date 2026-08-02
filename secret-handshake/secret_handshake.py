"""
Secret Handshake
"""


def commands(binary_str: str) -> list:
    """
    From binary int
    """
    
    actions = [
        'wink',
        'double blink',
        'close your eyes',
        'jump'
    ]
    action_list = []
    
    for index, binary in enumerate(reversed(binary_str)):
        if index <= 3:

            if binary == '0':
                continue
            
            else:
                action = actions[index]
                action_list.append(action)
        
        else:
            break
            
    if binary_str[0] == '1':
        action_list.reverse()
            
    return action_list
    
