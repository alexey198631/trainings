def isMyNumber(x):

    Secret = -5
    if x > Secret:
        return 1
    elif x < Secret:
        return -1
    elif x == Secret:
        return 0
    else:
        'check mistakes'



print(isMyNumber(-1))

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number.
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number

    returns: integer, the secret number
    '''
    guess = 1
    print(isMyNumber(guess))


    if isMyNumber(guess) == 0:
        return guess

    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == -1:
            guess += 1
            print('g-',guess)
        elif sign == 0:
            foundNumber = True
            print('=',guess)
        else:
            guess -= 1
            print('g+', guess)
    return guess


print(jumpAndBackpedal(isMyNumber))