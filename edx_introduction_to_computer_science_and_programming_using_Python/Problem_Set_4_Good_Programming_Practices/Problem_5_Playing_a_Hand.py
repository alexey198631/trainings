from Problem_1_Word_Scores import getWordScore
from Problem_2_Dealing_with_Hands import updateHand
from Problem_4_Hand_Length import calculateHandlen
from Word_Game import displayHand
from Problem_3_Valid_Words import isValidWord


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    inp = ""
    uh = updateHand(hand, inp)
    total = 0

    while calculateHandlen(uh) > 0:
        print('Current hand:', end=' ')
        displayHand(uh)
        inp = input('Enter word, or a "." to indicate that you are finished: ')
        if inp == ".":
            print('Goodbye! Total score: ', total, 'points')
            break
        else:
            if isValidWord(inp, uh, wordList) == True:

                pts = getWordScore(inp, n)
                total = total + pts
                print("' ", inp, " earned", pts, "points. Total: ", total, "points")
                print()
                uh = updateHand(uh, inp)

            else:
                print('Invalid word, please try again.')
                print()
    else:
        if calculateHandlen(uh) == 0:
            print('Run out of letters. Total score: ', total, 'points.')