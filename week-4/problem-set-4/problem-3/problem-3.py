def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # Make a copy of the hand so you don't mutate it
    handCopy = dict(hand)

    if word in wordList:
        for letter in word:
            # If the Letter is not in the hand, return False
            if letter not in hand.keys():
                return False
            # If there is no more of that letter in the Hand, return False
            if handCopy[letter] == 0:
                return False
            # Takes the number of letters in the hand down by one
            handCopy[letter] -= 1
        # If all of this is okay return True
        return True
    # If the word isn't valid, return False
    else:
        return False