from Problem_1_Is_the_Word_Guessed import isWordGuessed
from Problem_2_Getting_the_Users_Guess import getGuessedWord
from Problem_3_Printing_Out_all_Available_Letters import getAvailableLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is, ', len(secretWord), 'letters long.')

    attempts = 8
    mistakesMade = 0

    while attempts > 0:

        while not isWordGuessed(secretWord, lettersGuessed) and attempts > 0:

            print('-------------')

            print('You have ', attempts, ' guesses left.')

            print('Available letters: ', getAvailableLetters(lettersGuessed))

            guess = input('Please guess a letter: ')
            guessInLowerCase = guess.lower()

            if guessInLowerCase not in lettersGuessed:
                lettersGuessed.append(guessInLowerCase)

                if guessInLowerCase in secretWord:
                    print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
                else:
                    print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
                    attempts -= 1
                    mistakesMade += 1
            else:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))

                mistakesMade += 1
        else:
            print('-------------')
            if attempts != 0:
                print('Congratulations, you won!')
                break
            else:
                print('Sorry, you ran out of guesses. The word was ', secretWord)