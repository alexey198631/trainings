def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    sw = []

    for l in secretWord:
        if l in lettersGuessed:
            sw.append(True)
        else:
            sw.append(False)
    ans = True
    for tf in sw:
        ans = ans * tf

    return bool(ans)
