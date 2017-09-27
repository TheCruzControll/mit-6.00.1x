# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in list(secretWord):
        if i in lettersGuessed:
            continue
        else:
            return False
    return True


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

