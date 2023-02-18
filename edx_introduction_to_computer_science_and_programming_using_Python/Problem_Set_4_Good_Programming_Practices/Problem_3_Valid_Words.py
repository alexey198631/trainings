"""
At this point, we have written code to generate a random hand and display that hand to the user.
We can also ask the user for a word (Python's input) and score the word (using your getWordScore).
However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game.
A valid word is in the word list; and it is composed entirely of letters from the current hand.

Implement the isValidWord function.
"""
from Word_Game import getFrequencyDict


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    w = getFrequencyDict(word)
    f = []
    k = 1
    s = False
    y = 0
    copyhand = hand.copy()

    for i in w:
        if (i in copyhand.keys()) and (w[i] <= copyhand[i]):
            f.append(True)
            copyhand[i] = copyhand[i] - 1
        else:
            f.append(False)

    for n in f:
        k = k * n

    if k == 1:
        while y < len(wordList):
            if wordList[y] == word:
                s = True
            y += 1
    return s