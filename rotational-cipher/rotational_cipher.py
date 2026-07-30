"""
Rotational Cipher exercise
"""


def rotate(text, key):
    """
    Rotational cipher
    """
    
    text_list = []
    for char in text:
        if char.isspace():
            text_list.append(' ')
            
        elif char.isalpha():
            num_representation = ord(char)
            
            if num_representation >= 65 and num_representation < 97:
            
                cipher_char = num_representation + key
                check = cipher_char - 65
                
                if check >= 26:
                    circ = check - 26
                    cipher_char = 65 + circ 
            
            if num_representation >= 97:
                
                cipher_char = num_representation + key
                check = cipher_char - 97
                
                if check >= 26:
                    circ = check - 26
                    cipher_char =  97 + circ
            
            char_representation = chr(cipher_char)
        
            text_list.append(char_representation)
        
        else:
            text_list.append(char)

    cipher_text = ''.join(text_list)
    return cipher_text
    
    
