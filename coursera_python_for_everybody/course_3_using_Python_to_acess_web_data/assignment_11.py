"""
Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.
Data Files
We provide two files for this assignment.
One is a sample file where we give you the sum for your testing and the other is the actual data you need to process
for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_1552728.txt (There are 43 values and the sum ends with 276)

The basic outline of this problem is to read the file, look for integers using the re.findall(),
looking for a regular expression of '[0-9]+'
and then converting the extracted strings to integers and summing up the integers.
"""
import re

# import file with text and number in it
name = "data_files/regex_sum_1552728.txt"
handle = open(name)

# list for numbers from the text
numlist = list()

# pattern to find any number
pattern = '[0-9]+'

# checking all lines for numbers with pattern
for line in handle:
    line = line.rstrip()
    new = re.findall(pattern, line)
    x = len(new)
    # if a line contains numbers, transform them in float and append to the number list
    if x >= 1:
        for n in new:
            num = int(n)
            numlist.append(num)

# sum of all elements in the number list
print("Sum:", sum(numlist))