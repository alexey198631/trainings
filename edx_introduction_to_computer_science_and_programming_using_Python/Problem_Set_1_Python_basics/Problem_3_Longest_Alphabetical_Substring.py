"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print

Longest substring in alphabetical order is: abc
"""


def the_longest_alpabetical_substring(some_string):
    length = 0
    temp = 0
    s = some_string
    for i in range(0, len(s) - 1):
        temp = s[i]
        while i != (len(s) - 1) and s[i] <= s[i + 1]:
            temp += s[i + 1]
            i += 1
        if len(temp) > length:
            length = len(temp)
            longest = temp
    print('Longest substring in alphabetical order is: ' + str(longest))


the_longest_alpabetical_substring('azcbobobegghakl')
the_longest_alpabetical_substring('abcbcd')
