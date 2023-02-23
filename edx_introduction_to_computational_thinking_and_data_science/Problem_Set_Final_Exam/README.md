#### MyPython - trainings

## Coursera - Introduction to Computer Science and Programming Using Python

### Final Exam Coding Problems

#### Problem 3

A Monte Carlo simulation of drawing 3 balls out of a bucket containing 4 red and 4 green balls.
Balls are not replaced once drawn. Returns a float - the fraction of times 3  balls of the same color were drawn in the first 3 draws.

#### Problem 4

Implementation functions `makeHistogram`, that produces a histogram of values with numBins bins and the indicated labels
and for the x and y axis, `getAverage` that returns the mean and calls makeHistogram to produce a histogram of the longest runs for all the trials. There should be 10 bins in the histogram.

<img src="https://github.com/alexey198631/trainings/blob/main/edx_introduction_to_computational_thinking_and_data_science/Problem_Set_Final_Exam/data_files/p4.png" alt="p4" width="600" align="center">

#### Problem 6 Find combination

Implementation of a function that meets the specifications:

```def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    ```

#### Problem 8

Population growth simulation of foxes and rabbits in a forest.

<img src="https://github.com/alexey198631/trainings/blob/main/edx_introduction_to_computational_thinking_and_data_science/Problem_Set_Final_Exam/data_files/p81.png" alt="p81" width="600" align="center">

Assume `MAXRABBITPOP = 1000`, `CURRENTRABBITPOP = 500`, `CURRENTFOXPOP = 30`, numSteps = `200`. Plot two curves, one for the rabbit population and one for the fox population.

<img src="https://github.com/alexey198631/trainings/blob/main/edx_introduction_to_computational_thinking_and_data_science/Problem_Set_Final_Exam/data_files/p82.png" alt="p82" width="600" align="center">

Using of polyfit to find the coefficients of a 2nd degree polynomial for the rabbit curve and the same for the fox curve. Then use polyval to evaluation the 2nd degree polynomial and plot it.

<img src="https://github.com/alexey198631/trainings/blob/main/edx_introduction_to_computational_thinking_and_data_science/Problem_Set_Final_Exam/data_files/p83.png" alt="p83" width="600" align="center">
