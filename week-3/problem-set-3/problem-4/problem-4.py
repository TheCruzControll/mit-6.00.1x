def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    wordlength = len(secretWord) 
    guessesLeft = 8
    lettersGuessed = [] 
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(wordlength) + " letters long.")
    print ("-------------")
    
    while guessesLeft > 0:
        print ("You have " + str(guessesLeft) + " guesses left.")
        print ("Available letters: " + str(getAvailableLetters(lettersGuessed)))
        computerGuess = input("Please guess a letter: ")
        
        if computerGuess.lower() not in lettersGuessed:
            lettersGuessed.append(computerGuess.lower())
            if computerGuess.lower() in secretWord:
                print ("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
                if str(getGuessedWord(secretWord, lettersGuessed)) == secretWord:
                    print ("------------")
                    print ("Congratulations, you won!")
                    break
            elif computerGuess.lower() not in secretWord:
                print ("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
                guessesLeft -= 1
        elif computerGuess.lower() in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
        print ("------------")
    
    if computerGuess.lower() not in secretWord:
        print ("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")