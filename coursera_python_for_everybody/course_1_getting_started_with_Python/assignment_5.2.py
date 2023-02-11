"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except
and put out an appropriate message and ignore the number.

Enter 7, 2, bob, 10, and 4 and match the output below.
Invalid input
Maximum is 10
Minimum is 2

elif num != int or float : break
print("Enter number, not a word!")
"""
maximum = None
minimum = None

while True:
    number = input("Please, enter a number: ")
    if number == 'done' :
        break
    try:
        int_number = int(number)
        if minimum is None :
            minimum = int_number
        elif int_number < minimum:
            minimum = int_number
        if maximum is None :
            maximum = int_number
        elif int_number > maximum :
            maximum = int_number
    except:
         print("Enter number, not a word!")
    continue

print(f'\nMaximum is {maximum}\nMinimum is {minimum}')