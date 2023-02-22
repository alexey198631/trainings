#### MyPython - trainings

## Coursera - Introduction to Computer Science and Programming Using Python - Unit 3

### Coding Exercises

- **Exercise stdDevOfLengths(L)**: the function that takes in a list of strings and outputs the standard deviation of the lengths of the strings. Return float('NaN') if L is empty

- **Exercise - Ball the same color Monte Carlo simulation**:

You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the bucket, you don't replace it. What is the probability of drawing 3 balls of the same color? It is a Monte Carlo simulation to solve the above problem.

### Problem Set 3

#### Introduction

In this problem set, using Python and Pylab, you will design and implement a stochastic simulation of patient and virus population dynamics, and reach conclusions about treatment regimens based on the simulation results.

#### Background: Viruses, Drug Treatments, and Computational Models

Viruses such as HIV and H1N1 represent a significant challenge to modern medicine. One of the reasons that they are so difficult to treat is their ability to evolve.

As you may know from introductory biology classes, the traits of an organism are determined by its genetic code. When organisms reproduce, their offspring will inherit genetic information from their parent. This genetic information will be modified, either because of mixing of the two parents' genetic information, or through mutations in the genome replication process, thus introducing diversity into a population.

Viruses are no exception. Two characteristics of viruses make them particularly difficult to treat. The first is that their replication mechanism often lacks the error checking mechanisms that are present in more complex organisms. This speeds up the rate of mutation. Secondly, viruses replicate extremely quickly (orders of magnitude faster than humans) -- thus, while we may be used to thinking of evolution as a process which occurs over long time scales, populations of viruses can undergo substantial evolutionary changes within a single patient over the course of treatment.

These two characteristics allow a virus population to acquire genetic resistance to therapy quickly. In this problem set, we will make use of simulations to explore the effect of introducing drugs on the virus population and determine how best to address these treatment challenges within a simplified model.

Computational modeling has played an important role in the study of viruses such as HIV (for example, see this paper, by MIT graduate David Ho). In this problem, we will implement a highly simplified stochastic model of virus population dynamics. Many details have been swept under the rug (host cells are not explicitly modeled and the size of the population is several orders of magnitude less than the size of actual virus populations). Nevertheless, our model exhibits biologically relevant characteristics and will give you a chance to analyze and interpret interesting simulation data.

#### Spread of a Virus in a Person

In reality, diseases are caused by viruses and have to be treated with medicine, so in the remainder of this problem set, we'll be looking at a detailed simulation of the spread of a virus within a person. We've provided you with skeleton code in `ps3b.py`.

#### Problem 1: Implementing a Simple Simulation (No Drug Treatment)

A trivial model of the virus population - the patient does not take any drugs and the viruses do not acquire resistance to drugs. We simply model the virus population inside a patient as if it were left untreated.

#### Problem 2-1: Running and Analyzing a Simple Simulation (No Drug Treatment)

Understanding the population dynamics before introducing any drug

<img src="https://github.com/alexey198631/trainings/tree/main/edx_introduction_to_computational_thinking_and_data_science/Problem_Set_3_Running_and_Analyzing_Simulation/data_files/pr2.png" alt="course picture" width="200" align="center">

#### Problem 3: Implementing a Simulation With Drugs



#### Problem 5: Running and Analyzing a Simulation With a Drug

The program calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. Fixed monthly payment is a constant amount that will be paid each month.

- **Problem_3_Using_Bisection_Search_to_Make_the_Program_Faster.py**:

The program uses bisection search to determine the minimum fixed monthly payment
