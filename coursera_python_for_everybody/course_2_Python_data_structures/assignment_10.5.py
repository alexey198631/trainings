"""
10.2 Write a program to read through the mbox-short.txt
and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour.
"""

# file mbox-short.txt is in 'data_files' forlder

file_name = 'data_files/' + input("# Use the file name mbox-short.txt as the file name\nEnter file name: ")

# Open the file and read it line by line
with open(file_name) as file:
    count = 0
    temp = {}
    for line in file:
        if line.startswith('From '):
            hour = line.split(' ')[6].split(':')[0]
            temp[hour] = temp.get(hour, 0) + 1

# sort in order from earlier time to later time
counts = sorted(temp.items())

#print final result
for hours, times in counts:
    print(hours, times)