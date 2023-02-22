"""
You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the bucket,
you don't replace it. What is the probability of drawing 3 balls of the same color?

Write a Monte Carlo simulation to solve the above problem. Feel free to write a helper function if you wish.
"""
import random


# helper function 1 - random ball drawing without replacement
def randomball(q_red, q_green, trials):
    lst = []
    result = []
    # making the list of green and red balls in necessary quantity
    for i in range(q_red):
        lst.append('red')
    for j in range(q_green):
        lst.append('green')
    # random drawing of the balls without replacing it (removing from the bucket)
    while trials > 0:
        # from random.sample -> list with 1 element, [0] - you take this one element, not the list
        ball = random.sample(lst, 1)[0]
        lst.remove(ball)
        result.append(ball)
        trials -= 1
    return result


# helper function 2 - checks whether all balls are the same color
def all_one_color(lst):
    check = set(lst)
    if len(check) == 1:
        return 1
    else:
        return 0


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    tr = 0
    total = 0
    for i in range(numTrials):
        if all_one_color(randomball(3, 3, 3)) == 1:
            tr += 1
            total += 1
        else:
            total += 1

    return tr / total


print(noReplacementSimulation(5000))  # Expected a value between 0.088 and 0.112
