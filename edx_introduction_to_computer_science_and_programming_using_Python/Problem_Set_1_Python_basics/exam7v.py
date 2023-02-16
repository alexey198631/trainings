"""
       word, a string of length > 1 of alphabetical
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26)
       times its distance from start of word.
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters.
       The first parameter to f is the highest letter score,
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the
           score for 'adD' is 12
    """
word = 'bbU'

al = "abcdefghijklmnopqrstuvwxyz"


#creation of a dictionary with points

def alpha(al):
    alpha = {}
    for i in range(0,len(al)):
        alpha.update({al[i]: i+1})
    return alpha

#print(alpha(al))
#creation of scores * location - > list of integers

def pfl(word):
    num = list()
    ranks = alpha(al)
    for i in range(0,len(word)):
        l = word[i].lower()
        for k in ranks.keys():
            if k == l:
                num.append(ranks[k]*i)

    return num

print('pfl', pfl(word))

#determine the first scores and delete this scores - > first

def first(word):
    num = pfl(word)
    max = 0
    for n in range(0,len(num)):
        if num[n] > max:
            max = num[n]

    return max

print(first(word))
#determine the second scores and delete this scores - > second

def second(word):
    max = first(word)
    num = pfl(word)
    num.remove(max)
    second = 0
    for n in range(0, len(num)):
        if num[n] > second:
            second = num[n]

    return second

print(second(word))

def f(a,b):
    return int(a + b)

def score(word, f):
    if len(word) > 1:
        ans = f(int(first(word)),int(second(word)))
        return ans
    else:
        return 0

print(score(word, f))