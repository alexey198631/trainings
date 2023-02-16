def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    '''
    for l in secretWord:
        if l not in sw:
            sw.append(l)
    '''
    # FILL IN YOUR CODE HERE...
    sw = []
    t = ''

    for l in secretWord:
        if l in lettersGuessed:
            sw.append(l)
        else: sw.append('_')
    t = ''.join(sw)
    return t



print(getGuessedWord('durian', ['h', 'a', 'r', 'd']))




#secretWord = 'apple'
#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']