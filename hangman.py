def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    copy = list(secretWord)
    for letter in secretWord:
        if letter in lettersGuessed:
            copy.remove(letter)
    if copy == []:
        return True
    else:
        return False
        
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    copy = secretWord
    for letter in secretWord:
        if not letter in lettersGuessed:
            copy = copy.replace(letter, '_ ')
    return copy
    

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    copy = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in copy:
            copy.remove(letter)
    return ''.join(copy)
    
    
import string
availableLetters = string.ascii_lowercase
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
    lettersGuessed = ''
    mistakesMade = 8
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %i letters long" % len(secretWord)
    while not isWordGuessed(secretWord, lettersGuessed):
        print "-----------"
        if mistakesMade == 0:
            return end(secretWord)
        print "You have %i guesses left." % mistakesMade
        print "Available letters: %s" % getAvailableLetters(lettersGuessed)
        print "Please guess a letter: ",
        guess = str(raw_input())
        guess = guess.lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed += guess
            if len(guess) > 1 or len(guess) < 1:
                print "Invalid input. Please try again."
            elif guess not in getGuessedWord(secretWord, lettersGuessed):
                mistakesMade -= 1
                print "Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed)
            else:
                print "Good guess: ", getGuessedWord(secretWord, lettersGuessed)
    print "-----------"
    print "Congratulations, you won!"
def end(x):
    print "Sorry, you ran out of guesses. The word was %s." % x