import random
from Problem_4_The_Game import hangman

WORDLIST_FILENAME = "data_files/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    four = []
    length = int(input('Choose the length of your word, please! '))
    for word in wordlist:
        if len(word) == length:
            four.append(word)

    return random.choice(four)


wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()

hangman(secretWord)