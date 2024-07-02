def is_convenient(letter): 



Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
Right: y, u, i, o, p, h, j, k, l, n, m



def is_comfortable_word(word):
    # Define the sets of characters for each hand
    left_hand = 'qwertasdfgzxcvb'
    right_hand = 'yuiophjklnm'
    
    # Function to determine which hand a character belongs to
    def get_hand(char):
        if char in left_hand:
            return 'left'
        elif char in right_hand:
            return 'right'
        else:
            return None  # This case won't occur as per problem statement
    
    # Check if the word is empty, if so, return False
    if not word:
        return False
    
    # Get the hand of the first character
    current_hand = get_hand(word[0])
    
    # Iterate through the word using index and check alternation
    for i in range(1, len(word)):
        next_hand = get_hand(word[i])
        if next_hand == current_hand:
            return False  # If the same hand is used consecutively, return False
        current_hand = next_hand  # Update the current hand
    
    return True

# Example usage
print(is_comfortable_word("alternating"))  # Example case, should return True if valid
print(is_comfortable_word("apple"))        # Should return False




def comfortable_word(word):
    left_hand = set('qwertasdfgzxcvb')
    right_hand = set ('yuiophjklnm')
    
    for char in word:
        if (char in left_hand) and (word.index(char) % 2 != 0):
            return False
        if (char in right_hand) and (word.index(char) % 2 == 0):
            return False
    return True

    # TODO: complete
    return True