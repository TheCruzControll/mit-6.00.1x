def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = []
    for i in list(secretWord):
        if i in lettersGuessed:
            word.append(i)
        else:
            word.append('_ ')
    return "".join(word)