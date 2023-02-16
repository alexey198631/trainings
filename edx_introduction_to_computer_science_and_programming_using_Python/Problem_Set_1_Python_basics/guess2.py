x = input("Please think of a number between 0 and 100! ")

low = 0
high = 100
ans = (low + high)/2

print('Is your secret number?', ans)
c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while not c == "c":
    if c == "h":
        high = ans
    elif c == "l":
        low = ans
    else: print('Sorry, I did not understand your input.')
    ans = int((low + high) / 2)
    print('Is your secret number?', ans)
    c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print('Game over. Your secret number was: ', ans)