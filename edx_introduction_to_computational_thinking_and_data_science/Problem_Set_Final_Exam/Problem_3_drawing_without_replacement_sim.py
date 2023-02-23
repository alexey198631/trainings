"""
You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket.
Assume that once you draw a ball out of the bucket, you don't replace it. You draw 3 balls.

Write a Monte Carlo simulation that meets the specifications below. Feel free to write a helper function if you wish.
"""
import random


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    greens = 'green'
    reds = 'red'
    count = 0

    for n in range(numTrials):
        bucket = [greens] * 4 + [reds] * 4
        out = []
        for i in range(3):
            ball = random.choice(bucket)
            out.append(ball)
            bucket.remove(ball)
        if out[0] == out[1] == out[2]:
            count += 1

    return count / numTrials


# testing
#print(drawing_without_replacement_sim(1000))