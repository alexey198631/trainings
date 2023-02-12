"""
8.5 Open the file mbox-short.txt and read it line by line.
When you find a line that starts with 'From ' like the following line:
'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
You will parse the From line using split() and print out the second word in the line
(i.e. the entire address of the person who sent the message).
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

# file mbox-short.txt is in 'data_files' forlder

file_name = 'data_files/' + input("# Use the file name mbox-short.txt as the file name\nEnter file name: ")

# Open the file and read it line by line
with open(file_name) as file:
    count = 0
    temp = []
    for line in file:
        if line.startswith('From '):
            words = line.split()
            if len(words) > 1:
                if words[1] not in temp:
                    temp.append(words[1])
                    print(words[1])
                count += 1

print(f'There were {count} emails from {len(temp)} addresses')