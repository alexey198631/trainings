"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form:
'X-DSPAM-Confidence:    0.8475'
Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

# file mbox-short.txt is in 'data_files' forlder


file_name = 'data_files/' + input("# Use the file name mbox-short.txt as the file name\nEnter file name: ")

file = open(file_name)
n = 0  # number of lines
sm = 0  # for  sum
number = 0

for line in file:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    n = n + 1
    # find the position of the number
    start = line.find(":") + 1
    end = len(line)
    # extract the number from the string and convert it to a float
    number = float(line[start:end])
    sm = sm + number

avg = round((sm / n), 2)
print("Confidence average value: ", avg)