def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    s = list(string.ascii_lowercase)
    for i in lettersGuessed:
        if i in s:
            s.remove(i)
    return "".join(s)