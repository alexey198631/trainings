

animals = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}


#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest = 0
    p = ""

    for k in aDict:

        if biggest <= len(aDict[k]):
            biggest = len(aDict[k])
            p = k
    return p


print(biggest(animals))

"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result

"""