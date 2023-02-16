def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alp = 'abcdefghijklmnopqrstuvwxyz'

    sw = []
    t = ''
    st = ''

    for l in alp:
        if l in lettersGuessed:
            sw.append('')
        else:
            sw.append(l)
    st = sorted(sw)
    t = ''.join(st)
    return t

print(getAvailableLetters(['a','z']))