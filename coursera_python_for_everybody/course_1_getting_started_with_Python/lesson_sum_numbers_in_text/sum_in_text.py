import re

# import file with text and number in it
name = "regex_sum_1552728.txt"
handle = open(name)

# list for numbers from the text
numlist = list()

# pattern to find any number
pattern = '[0-9]+'

# checking all lines for numbers with pattern
for line in handle:
    line = line.rstrip()
    new = re.findall(pattern, line)
    print(new)
    x = len(new)
    # if a line contains numbers, transform them in float and append to the number list
    if x >= 1:
        for n in new:
            num = float(n)
            numlist.append(num)

# sum of all elements in the number list
print("Sum:", sum(numlist))