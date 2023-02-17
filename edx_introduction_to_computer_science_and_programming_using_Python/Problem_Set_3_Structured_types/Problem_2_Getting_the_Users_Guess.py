def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    sw = []
    t = ''
    for l in secretWord:
        if l in lettersGuessed:
            sw.append(l)
        else:
            sw.append(' _ ')
    t = ' '.join(sw)

    return t
