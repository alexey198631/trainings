listA = [1, 4, 3, 0]

dict ={'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}


#listA = listA.sort

listA.pop()

del dict['b']

#print(dict)

#print(listA)

#print(dict.values())

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    lent = 0
    values = aDict.values()
    for l in values:

            lent = len(l)
            while lent > 0:
                count += 1
                lent -= 1

    return count

print(how_many(animals))

"""


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        result += len(value)
    return result

def how_many(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result



"""