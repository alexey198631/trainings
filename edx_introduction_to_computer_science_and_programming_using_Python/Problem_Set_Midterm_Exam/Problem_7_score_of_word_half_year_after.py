"""
Write a function called score that meets the specifications below.

def score(word, f):
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


After half a year learning Python, I decided to re-write my code for this task
"""

# simle sum
def f(a, b):
    return int(a + b)


def score(word, f):
    # creation of a dictionary with points
    al = "abcdefghijklmnopqrstuvwxyz"
    letter_scores = {al[i]: i + 1 for i in range(len(al))}
    # computing the score for each letter in the word
    letter_scores_word = [letter_scores[w.lower()] * i for i, w in enumerate(word)]
    # sort the letter scores in descending order and take the two highest ones
    sorted_scores = sorted(letter_scores_word, reverse=True)[:2]
    # applying the function f to the two highest scores
    return f(sorted_scores[0], sorted_scores[1])

example = 'adD'
print(score(example, f)) # output 12
example2 = 'test'
print(score(example2, f)) # output 98

