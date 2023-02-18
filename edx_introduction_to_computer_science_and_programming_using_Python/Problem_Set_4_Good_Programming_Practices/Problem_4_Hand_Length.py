"""
We are now ready to begin writing the code that interacts with the player.
We'll be implementing the playHand function.

This function allows the user to play out a single hand.
First, though, you'll need to implement the helper calculate Handlen function,
which can be done in under five lines of code.
"""


def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    s = 0
    for k in hand:
        s = s + hand[k]
    return s