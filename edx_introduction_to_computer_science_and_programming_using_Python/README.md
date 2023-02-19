##### MyPython - trainings

### Summary

This project contains assignments that I found interesting and solved during the completion of the following course:

## [edX - MITx: 6.00.1x - Introduction to Computer Science and Programming Using Python](https://www.edx.org/course/introduction-to-computer-science-and-programming-7?index=product&queryID=ffa27a743e81f3397da91aefee857fe1&position=1)

### [Unit 1: Python Basics](https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computer_science_and_programming_using_Python/Problem_Set_1_Python_basics)

- **Problem_1_Counting_Vowels.py**: the program that counts up the number of vowels contained in the string s
- **Problem_2_Counting_Bobs.py**: the program that prints the number of times the string 'bob' occurs in s
- **Problem_3_Longest_Alphabetical_Substring.py**: the program that prints the longest substring of s in which the letters occur in alphabetical

### [Unit 2: Simple Programs](https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computer_science_and_programming_using_Python/Problem_Set_2_Simple_programs)

#### [Exercises](https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computer_science_and_programming_using_Python/Problem_Set_2_Simple_programs/exercises)

- **Guess_my_number**: the program guesses a secret number
- **power iter**: the iterative function calculates the exponential using iteration
- **power recur**:the iterative function calculates the exponential using recursion
- **gcd iter**: the program determines the greatest common divisor of two positive integers using iteration
- **gcd recur**: the program determines the greatest common divisor of two positive integers using recursion
- **is in**: the program determines a character is in a string using bisection search
- **Polysum**: the program determines the perimeter of the regular polygon

#### Problem set 2

- **Problem_1_Problem_1_Paying_Debt_off_in_a_Year.py**: The program calculates the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
- **Problem_2_Paying_Debt_Off_in_a_Year.py**: The program calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. Fixed monthly payment is a constant amount that will be paid each month.
- **Problem_3_Using_Bisection_Search_to_Make_the_Program_Faster.py**: The program uses bisection search to determine the minimum fixed monthly payment

### [Unit 3: Structured types](https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computer_science_and_programming_using_Python/Problem_Set_3_Structured_types)

#### [Exercises](https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computer_science_and_programming_using_Python/Problem_Set_3_Structured_types/exercise)

- **Exercise_odd_tuples.py**: the procedure takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one.
- **Exercise_biggest.py**: the procedure returns the key corresponding to the entry with the largest number of values associated with it.
- **Exercise_how_many.py**: the procedure returns the sum of the number of values associated with a dictionary.

#### The classic wordgame Hangman

- **Problem 1 - Is the Word Guessed**: 3 simple functions that will help easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.
- **Problem 2 - Getting the User's Guess**: The function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. There will be no too different from isWordGuessed!
- **Problem 3 - Printing Out all Available Letters**: The function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
- **Problem 4 - The Game**: The function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer.
- **Hangman**: App combining all parts

### [Midterm EXAM coding problems](https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computer_science_and_programming_using_Python/Problem_Set_Midterm_Exam)

- **Problem_3 Fix errors**: isMyNumber: Procedure that hides a secret number, jumpAndBackpedal: Procedure that determine a secret number.
- **Problem 4 Get Sublists**: A function called getSublists, which takes as parameters a list of integers named L and an integer named n.
- **Problem 5 Unique values in a Dictionary**: A Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict)
- **Problem 6 Recursive Sum of digits**: A recursive Python function, given a non-negative integer N, calculates and return the sum of its digits.
- **Problem 7 Score of Word**: A function called score that meets the specifications.
- **Problem 7 Score of Word - half year after**: A function called score that meets the specifications. After half a year learning Python, I decided to re-write my code for this problem

### [Unit 4: Good Programming Practices](https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computer_science_and_programming_using_Python/Problem_Set_4_Good_Programming_Practices)

### Wordgame

- **Problem 1 - Word Scores**: Code that allows us to calculate the score for a single word
- **Problem 2 - Dealing with Hands**: Removing letters from a hand
- **Problem 3 - Valid Words**: Code to verify that a word given by a player obeys the rules of the game
- **Problem 4 - Hand Length**: The helper calculateHandlen function
- **Problem 5 - Playing a Hand**: Allows the user to play the given hand
- **Problem 6 - Playing a Game**: A game consists of playing multiple hands. The code implements the playGame function.
- **Word Game**: Full code for the Word Game
- **Word Game with Computer**: Computer Choosing a Word and Playing a Hand

### [Unit 5: Object Oriented Programming](https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computer_science_and_programming_using_Python/Problem_Set_5_Object_Oriented_Programming)

#### Exercises

- **Exercise Coordinate**: definition of two methods for the Coordinate class
- **Exercise genPrimes**: the generator returns the sequence of prime numbers on successive calls to its next() method
- **Exercise intset**: defining an intersect method that returns a new intSet containing elements that appear in both sets
- **Exercise hand**: an object-oriented implementation of the hand from the word game problem of

#### [Problem Set 4](https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computer_science_and_programming_using_Python/Problem_Set_4_Good_Programming_Practices)

- **Problem 1 - Build the Shift Dictionary and Apply Shift**: a dictionary that can be used to apply a cipher to a letter, apply the Caesar Cipher to message_text with the input shift
- **Problem 2 - PlaintextMessage**: class creates an encoded version of the message + methods for changing the encoding
- **Problem 3 - CiphertextMessage**: init method, decrypt message method function
- **Problem 4 - Decrypt a Story**: CiphertextMessage object using the story string and use decrypt_message to return
the appropriate shift value and unencrypted story string
- **Caesar Cipher**:implementation of cipher and decipher app including all problems 1-4 and helper code

### [Final Exam Coding Problems](https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computer_science_and_programming_using_Python/Final_Exam)

- **Problem 3 Is triangular**: The function returns True if k is triangular and False if not. A triangular number is a number obtained by the continued summation of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.
- **Problem 4 Is list permutation**: The function takes in two lists and calculates whether they are permutations of each other. The lists can contain both integers and strings.
- **Problem 5 Cipher**:The function decodes string using two dictionaries map_from and map_to
- **Problem 6 USResident**: The file contains a Person class and a USResident class (a subclass of Person) with implemented methods
- **Problem 7 location class**: Campus class with methods: adding tent, removing tent, getting tents
