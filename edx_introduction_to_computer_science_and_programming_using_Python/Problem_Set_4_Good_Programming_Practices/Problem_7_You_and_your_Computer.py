"""
Now that your computer can choose a word, you need to give the computer the option to play.
Write the code that re-implements the playGame function.
You will modify the function to behave as described below in the function's comments.
As before, you should use the HAND_SIZE constant to determine the number of cards in a hand.
Be sure to try out different values for HAND_SIZE with your program.
"""
from Problem_1_Word_Scores import getWordScore
from Problem_2_Dealing_with_Hands import updateHand
from Problem_4_Hand_Length import calculateHandlen
from Word_Game import displayHand
from Problem_3_Valid_Words import isValidWord
from Problem_6_Playing_a_Game import HAND_SIZE


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet.
          Please play a new hand first!"

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    USER_CHOICE = "Enter n to deal a new hand, r to replay the last hand, or e to end game: "

    selection = input(USER_CHOICE)

    USER_CHOICE_TWO = 'Enter u to have yourself play, c to have the computer play: '

    n = HAND_SIZE
    last = {}

    while selection != 'e':
        if selection == 'n':
            selection_two = input(USER_CHOICE_TWO)
            while selection_two != 'u' and selection_two != 'c':
                print('Invalid command')
                selection_two = input(USER_CHOICE_TWO)
            else:
                hand = dealHand(n)
                last = hand.copy()
                if selection_two == 'u':
                    playHand(hand, wordList, n)
                elif selection_two == 'c':
                    compPlayHand(hand, wordList, n)
                else:
                    print('Invalid command.')


        elif selection == 'r':
            if last == {}:
                print('You have not played a hand yet. Please play a new hand first!')
                print()
            else:
                selection_two = input(USER_CHOICE_TWO)
                while selection_two != 'u' and selection_two != 'c':
                    print('Invalid command')
                    selection_two = input(USER_CHOICE_TWO)
                else:
                    if selection_two == 'u':
                        playHand(last, wordList, n)
                    elif selection_two == 'c':
                        compPlayHand(last, wordList, n)

        else:
            print('Invalid command.')

        selection = input(USER_CHOICE)